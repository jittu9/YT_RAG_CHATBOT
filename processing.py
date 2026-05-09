from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP
from logger import setup_logger

logger = setup_logger()

def split_text(transcript: str):
    logger.info("Splitting transcript into chunks")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.create_documents([transcript])