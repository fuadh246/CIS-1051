import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
embedding_model = OpenAIEmbeddings(api_key=openai_api_key)

DB_PATH = "embeddings/faiss_index"
def get_vector_store(documents):
    if not os.path.exists(DB_PATH):
        os.makedirs(DB_PATH)
    vector_db = FAISS.from_documents(documents, embedding_model)
    vector_db.save_local(DB_PATH)
    return vector_db

def search_vector_store(db, query: str):
    return db.similarity_search(query)
def load_vector_store():
    return FAISS.load_local(DB_PATH, embedding_model, allow_dangerous_deserialization=True)
