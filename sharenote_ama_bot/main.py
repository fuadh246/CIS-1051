import os
from fastapi import FastAPI, UploadFile, File, Form
from dotenv import load_dotenv
from openai import OpenAI
from langchain.schema import Document

from utils.file_reader import read_file
from utils.chunker import chunk_text
from utils.vector_store import get_vector_store, search_vector_store, load_vector_store

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

UPLOAD_DIR = "data/uploaded_docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

docs_db = load_vector_store()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    text = read_file(file_path)
    chunks = chunk_text(text)
    documents = [Document(page_content=chunk, metadata={"source": file.filename}) for chunk in chunks]
    global docs_db
    docs_db = get_vector_store(documents) 
    return {"status": "uploaded and indexed", "chunks": len(chunks)}

@app.get("/uploaded_files/")
async def get_uploaded_files():
    files = os.listdir(UPLOAD_DIR)
    return {"uploaded_files": files}

@app.get("/uploaded_files/{filename}")
async def get_uploaded_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            content = f.read()
        return {"filename": filename, "content": content}
    else:
        return {"error": "File not found"}

@app.post("/ask/")
async def ask_question(question: str = Form(...)):
    global docs_db
    if docs_db is None:
        return {"error": "No documents uploaded yet."}
    docs = search_vector_store(docs_db, question)
    context = "\n".join([doc.page_content for doc in docs])
    prompt = f"""Use the following context to answer the question:\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    answer = response.choices[0].message.content
    return {"answer": answer, "question": question}

@app.get("/")
async def root():
    return {"message": "Welcome to the ShareNote AMA bot"}
