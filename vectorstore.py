from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from config import EMBED_MODEL
from logger import setup_logger

logger = setup_logger()

def create_vector_store(chunks):
    logger.info("Creating embeddings and vector store")
    embeddings = OllamaEmbeddings(model=EMBED_MODEL)
    return FAISS.from_documents(chunks, embeddings)