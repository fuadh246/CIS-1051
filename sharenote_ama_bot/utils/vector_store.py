from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document
import os
from dotenv import load_dotenv
load_dotenv()

DB_DIR = "embeddings/faiss_index"
os.makedirs(DB_DIR, exist_ok=True)

embedding = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))

def get_vector_store(documents: list[Document]):
    if os.path.exists(os.path.join(DB_DIR, "index.faiss")):
        db = FAISS.load_local(DB_DIR, embeddings=embedding, allow_dangerous_deserialization=True)
        db.add_documents(documents)
    else:
        db = FAISS.from_documents(documents, embedding)
    db.save_local(DB_DIR)
    return db

def load_vector_store():
    if os.path.exists(os.path.join(DB_DIR, "index.faiss")):
        return FAISS.load_local(DB_DIR, embeddings=embedding, allow_dangerous_deserialization=True)
    return None

def search_vector_store(db, query: str):
    return db.similarity_search(query)
