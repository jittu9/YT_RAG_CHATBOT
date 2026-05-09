# YT_RAG_CHATBOT
# 🎥 YouTube Podcast RAG Chatbot

A Retrieval-Augmented Generation (RAG) based chatbot that allows users to chat with YouTube videos using transcript data.

This project extracts transcripts from YouTube videos, converts the transcript into embeddings using Ollama embeddings, stores them in a FAISS vector database, and retrieves relevant context to answer user questions using a locally deployed LLM.

---

# 🚀 Features

- Extract transcript directly from YouTube videos
- Supports multiple YouTube URL formats
- Uses FAISS vector database for similarity search
- Local LLM inference using Ollama
- Gradio-based interactive UI
- Modular LangChain pipeline
- Logging support for debugging and monitoring
- Retrieval-Augmented Generation (RAG) workflow

---

# 🏗️ Tech Stack

- Python
- LangChain
- Ollama
- FAISS
- Gradio
- YouTube Transcript API

---

# 📂 Project Structure

```bash
.
├── app.py               # Main Gradio application
├── chain_build.py       # LangChain RAG pipeline
├── config.py            # Model configuration
├── ingestion.py         # Transcript extraction logic
├── logger.py            # Logging setup
├── processing.py        # Text chunking logic
├── requirements.txt     # Dependencies
├── retriever.py         # Retriever creation
├── vectorstore.py       # FAISS vector store setup
└── main.py              # Entry point
```

---

# ⚙️ How It Works

1. User enters a YouTube video URL
2. Transcript is fetched using YouTube Transcript API
3. Transcript is split into chunks
4. Chunks are converted into embeddings
5. Embeddings are stored in FAISS vector database
6. Relevant chunks are retrieved based on user query
7. Retrieved context + user query are passed to local LLM
8. LLM generates contextual answers

---

# 🧠 Architecture Flow

```text
YouTube URL
     ↓
Transcript Extraction
     ↓
Text Chunking
     ↓
Embeddings Generation
     ↓
FAISS Vector Store
     ↓
Retriever
     ↓
LangChain RAG Pipeline
     ↓
Local LLM (Ollama)
     ↓
Answer Generation
```

---

# 📦 Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/youtube-rag-chatbot.git
cd youtube-rag-chatbot
```

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download and install Ollama:

urlOllama Official Websitehttps://ollama.com

Pull required models:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

---

# ▶️ Run Application

```bash
python app.py
```

Gradio app will start locally.

---

# 🖥️ Example Usage

1. Paste YouTube video URL
2. Click "Load Video"
3. Ask questions related to the video
4. Chatbot answers using transcript context only

---

# 📌 Example Questions

- What is the main topic of the video?
- Summarize the podcast discussion
- What did the speaker say about AI?
- Explain the key insights from the video

---

# 🔒 RAG Prompt Constraint

The chatbot is designed to:

- Answer ONLY from transcript context
- Avoid hallucinations
- Respond with "I don't know" when context is insufficient

---

# 📈 Future Improvements

- Persistent vector database storage
- Multi-video support
- Source citation support
- Chat history memory
- Separating Frontend and Backend using FASTAPI as bridge
- Streaming responses
- Docker deployment
- Authentication layer
- Cloud deployment

---

# 🧑‍💻 Author

Jitendra Damu

Cheers!
