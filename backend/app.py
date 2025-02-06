from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from ai import ChatBot


# Create a FastAPI instance
app = FastAPI()

# Create a ChatBot instance
chatbot = ChatBot()


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def index():
    return {"API Status": "Online"}


@app.get("/chat/query")
def fake_response(user_query: str):
    print("This is the user query:", user_query)
    response = chatbot.get_response(user_query)
    return JSONResponse(content=response, status_code=200)
