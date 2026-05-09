# import gradio as gr
# from ingestion import fetch_transcript, extract_video_id
# from processing import split_text
# from vectorstore import create_vector_store
# from retriever import get_retriever
# from chain_build import build_chain
# from logger import setup_logger

# logger = setup_logger()

# logger.info("Starting application...")

# # Global chain (shared after loading video)
# chain = None

# from logger import setup_logger




# def load_video(url):
#     """
#     Step 1: Validate URL
#     Step 2: Build pipeline
#     """
#     global chain

#     logger.info(f"Processing URL: {url}")

#     video_id = extract_video_id(url)
#     if not video_id:
#         logger.error("Invalid YouTube URL")
#         return "Invalid YouTube URL"

#     transcript = fetch_transcript(video_id)
#     if not transcript:
#         logger.error("Transcript not available")
#         return "Transcript not available for this video"

#     logger.info("Building pipeline...")

#     chunks = split_text(transcript)
#     vector_store = create_vector_store(chunks)
#     retriever = get_retriever(vector_store)
#     chain = build_chain(retriever)

#     logger.info("Pipeline ready!")

#     return "Video loaded successfully! You can now ask questions."


# def ask_question(question):
#     global chain

#     if chain is None:
#         return "Please load a YouTube video first."

#     logger.info(f"User question: {question}")

#     try:
#         response = chain.invoke(question)
#         return response
#     except Exception as e:
#         logger.exception("Error during inference")
#         return f"Error: {str(e)}"


# # ---- Gradio UI ----
# with gr.Blocks() as app:

#     gr.Markdown("# 🎥 YouTube Video Q&A")

#     with gr.Row():
#         url_input = gr.Textbox(label="YouTube URL", placeholder="Paste YouTube link here...")
#         load_btn = gr.Button("Load Video")

#     status_output = gr.Textbox(label="Status")

#     question_input = gr.Textbox(label="Ask a question")
#     answer_output = gr.Textbox(label="Answer")

#     load_btn.click(fn=load_video, inputs=url_input, outputs=status_output)
#     question_input.submit(fn=ask_question, inputs=question_input, outputs=answer_output)


# if __name__ == "__main__":
#     app.launch(server_name="0.0.0.0", server_port=7860)

import gradio as gr
from ingestion import fetch_transcript, extract_video_id
from processing import split_text
from vectorstore import create_vector_store
from retriever import get_retriever
from chain_build import build_chain
from logger import setup_logger

logger = setup_logger()

logger.info("Starting application...")

chain = None


# -----------------------------
# Load video pipeline
# -----------------------------
def load_video(url):
    global chain

    logger.info(f"Loading URL: {url}")

    video_id = extract_video_id(url)
    if not video_id:
        return None, "Invalid YouTube URL"

    transcript = fetch_transcript(video_id)
    if not transcript:
        return None, "Transcript not available"

    chunks = split_text(transcript)
    vector_store = create_vector_store(chunks)
    retriever = get_retriever(vector_store)
    chain = build_chain(retriever)

    return [], "Video loaded. Start chatting!"


# -----------------------------
# Chat function (core change)
# -----------------------------
def chat(message, history):
    global chain

    if chain is None:
        return "Please load a video first."

    logger.info(f"User: {message}")

    response = chain.invoke(message)

    logger.info(f"Bot: {response}")

    return response


# -----------------------------
# UI
# -----------------------------
with gr.Blocks() as app:

    gr.Markdown("YouTube Chat Assistant")

    url_input = gr.Textbox(label="YouTube URL")
    load_btn = gr.Button("Load Video")
    status = gr.Textbox()

    chatbot = gr.ChatInterface(
        fn=chat,
        title="Chat with Video",
    )

    load_btn.click(
        fn=load_video,
        inputs=url_input,
        outputs=[chatbot.chatbot, status]
    )


if __name__ == "__main__":
    app.launch(server_name="0.0.0.0", server_port=7860)