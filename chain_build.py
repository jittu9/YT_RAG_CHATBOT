from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from config import LLM_MODEL
from logger import setup_logger

logger = setup_logger()

def build_chain(retriever):
    logger.info("Building LangChain pipeline")

    llm = ChatOllama(model=LLM_MODEL)

    prompt = PromptTemplate(
        template="""
        You are a helpful assistant.
        Answer ONLY from the provided transcript context.
        If the context is insufficient, just say you don't know.

        {context}
        Question: {question}
        """,
        input_variables=['context', 'question']
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    parallel_chain = RunnableParallel({
        'context': retriever | RunnableLambda(format_docs),
        'question': RunnablePassthrough()
    })

    parser = StrOutputParser()

    return parallel_chain | prompt | llm | parser