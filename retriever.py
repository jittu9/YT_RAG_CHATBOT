from config import TOP_K
from logger import setup_logger

logger = setup_logger()

def get_retriever(vector_store):
    logger.info("Initializing retriever")
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": TOP_K}
    )