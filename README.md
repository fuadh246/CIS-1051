# ShareNote AMA Bot
**ShareNote AMA Bot** is a web-based Q&A assistant that allows users to upload documents and ask questions based on their content. It combines the power of OpenAI with document embeddings and a FastAPI backend, wrapped in a user-friendly Flask frontend.

## Features
* Upload `.txt`, `.pdf`, `.docx`, and `.doc` files
* Ask questions based on uploaded documents
* Uses OpenAI embeddings + GPT-3.5-turbo to answer contextually
* View all uploaded documents
* Session-based chat history and logs

## Tech Stack
* Frontend: Flask, Bootstrap 5
* Backend API: FastAPI
* Embeddings & LLMs: OpenAI + LangChain
* Vector Store: FAISS
* Deployment: Localhost (FastAPI: port `8000`, Flask: port `5000`)

## Installation
1. Clone the Repository
```bash
git clone https://github.com/yourusername/sharenote-ama-bot.git
cd sharenote-ama-bot
```

2. Set Up Python Environment
```bash
python -m venv ama-bot
source ama-bot/bin/activate
pip install -r requirements.txt

```
4. Add  `.env`
```bash
OPENAI_API_KEY= openai_key_here
```
## Usage
1. Start the Server site
```bash
cd sharenote_ama_bot
uvicorn main:app --reload
```
3. Start Flask Frontend
```bash
cd flask_app
python app.py
```

## API Endpoints
|Method | Endpoint | Description |
|-------|----------|-------------|
|POST | `/upload/`| Upload and index a file|
|PSOT|`/ask/`|Ask a question about the documents|
|GET|`/uploaded_files/`|List all uploaded files|
|GET|`/uploaded_files/{filename}`|Get content of specific file|

