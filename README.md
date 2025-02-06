# AI-Powered Chatbot for Supplier and Product Information
## Overview


AI-powered chatbot for supplier and product information enables natural language queries to a connected database. Utilizes an open-source large language model (LLM) combined with the LangGraph framework to coordinate agent workflows. Retrieves data from MySQL databases and generates concise, meaningful summaries with the LLM.

### Running the Project

#### Frontend
1. Install dependencies:
    ```bash
    npm install
    ```
2. Start the development server:
    ```bash
    npm run dev
    ```

#### Backend
1. Navigate to the backend directory:
    ```bash
    cd backend
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Install and configrue MySQL database.
    ```sql
    CREATE DATABASE InventoryDB;
    source ./database/sample_data.sql;
    ```
4. Create a `.env` file in the backend directory and add the following environment variables:
    ```env
    GROQ_API_KEY=<GROQ_API_KEY>
    MYSQL_HOST=<MYSQL_HOST>
    MYSQL_USER=<MYSQL_USER>
    MYSQL_PASSWORD=<MYSQL_PASSWORD>
    MYSQL_DB=<MYSQL_DB>
    ```
5. Start the backend server (using FastAPI with Uvicorn):
    ```bash
    uvicorn app:app --reload
    ```

#### Verification
- Open a browser and navigate to the frontend URL (usually http://localhost:5173).
- Interact with the chatbot to verify proper data fetching.
