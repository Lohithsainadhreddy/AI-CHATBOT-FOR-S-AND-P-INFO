from pydantic import BaseModel
from typing import List
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, GROQ_API_KEY
from sqlalchemy import create_engine
from langchain.sql_database import SQLDatabase
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq


# Define the state of the graph
class GraphState(BaseModel):
    question: str
    generation: str
    documents: List[str]


class ChatBot():
    def __init__(self):
        # Database
        self.db = self._configure_db()
        
        # Define workflow
        workflow = StateGraph(GraphState)
        workflow.add_node("retrieve", self.retrieve)
        workflow.add_edge(START, "retrieve")
        workflow.add_edge("retrieve", END)
        self.workflow = workflow.compile()
        
        # Initialize the LLM and toolkit
        llm = ChatGroq(
            groq_api_key=GROQ_API_KEY, 
            model_name="Llama3-8b-8192", 
            streaming=True
        )
        toolkit = SQLDatabaseToolkit(db=self.db, llm=llm)
        self.agent = create_sql_agent(
            llm=llm,
            toolkit=toolkit,
            verbose=True,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
        )

    def retrieve(self, state: GraphState) -> GraphState:
        question = state.question
        try:
            response = self.agent.run(question)
            return GraphState(question=question, generation=response, documents=[response])
        except Exception as e:
            return GraphState(question=question, generation=f"Error: {str(e)}", documents=[])
        
    def _configure_db(self):
        engine = create_engine(f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}?charset=utf8mb4&collation=utf8mb4_general_ci")
        return SQLDatabase(engine)
    
    def get_response(self, user_query):
        # try:
        #     response = self.agent.run(user_query)
        #     if "Error" in response:
        #         response = "Please ask a question related to the current database."
        # except Exception as e:
        #     return f"An error occurred: {str(e)}"
        # return response
        response = self.workflow.invoke(GraphState(question=user_query, generation="", documents=[]))
        return response.get("generation")


if __name__ == "__main__":
    chatbot = ChatBot()
    print("This the response:", chatbot.get_response("which supplier provides laptop?"))
