# 📚 Student RAG Assistant

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.3+-green.svg)
![FAISS](https://img.shields.io/badge/FAISS-CPU-orange.svg)
![Groq](https://img.shields.io/badge/Groq-Llama%203.3%2070B-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A powerful **Retrieval-Augmented Generation (RAG)** application designed to help students study efficiently. This tool ingests your study materials (PDFs, Textbooks, Notes) and allows you to ask questions, get summaries, and find specific information instantly using AI.

## 🚀 Features

- **Multi-Format Support**: Load PDFs, Text files, CSVs, Excel, Word docs, and JSON from the `data/` directory.
- **Smart Retrieval**: Uses **FAISS** for fast and accurate vector similarity search (<10ms).
- **High-Performance LLM**: Powered by **Groq** (using `llama-3.3-70b-versatile`) for lightning-fast responses (10-100x faster).
- **Local Embeddings**: Uses `SentenceTransformers` (paraphrase-MiniLM-L3-v2) to keep embedding generation local and free.
- **Persistent Storage**: Saves your vector index so you don't have to reload documents every time.
- **Auto-Rebuild Detection**: Automatically detects when data folder changes and rebuilds vector store.
- **Memory Optimized**: Reuses embedding models to avoid memory issues with large document sets.

## 🛠️ Tech Stack

- **Language**: Python 3.11
- **Framework**: [LangChain](https://www.langchain.com/) - RAG orchestration
- **LLM Provider**: [Groq Cloud](https://groq.com/) - Ultra-fast inference
- **Model**: `llama-3.3-70b-versatile` (70B parameters)
- **Embeddings**: `paraphrase-MiniLM-L3-v2` (SentenceTransformers, 384-dim, 60MB)
- **Vector Database**: [FAISS](https://github.com/facebookresearch/faiss) - Facebook AI Similarity Search
- **Document Parsing**: `PyMuPDF`, `pypdf`, `python-docx`, `openpyxl`
- **Environment**: Python venv with uv package manager

## 📂 Project Structure

```
RAG/
├── .venv/                  # Virtual Environment
├── data/                   # 📥 Place your study materials here (PDFs, TXTs)
├── RAG-Tutorials-main/
│   ├── .env                # 🔑 API Keys configuration
│   ├── app.py              # 🚀 Main application entry point
│   ├── requirements.txt    # Project dependencies
│   └── src/                # Core source code
│       ├── data_loader.py  # Document ingestion logic
│       ├── embedding.py    # Embedding generation
│       ├── search.py       # RAG search & LLM interaction
│       └── vectorstore.py  # FAISS database management
└── README.md               # Project documentation
```

## ⚡ Getting Started

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd RAG
```

### 2. Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r RAG-Tutorials-main/requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the `RAG-Tutorials-main` folder and add your Groq API key:

```properties
GROQ_API_KEY=gsk_your_actual_api_key_here
```
> **Note**: You can get a free API key from [Groq Console](https://console.groq.com/).

### 5. Add Your Data
Place your PDF textbooks, lecture notes (`.txt`), or past papers into the `data/` folder.

### 6. Run the Application
```bash
# Navigate to the source folder
cd RAG-Tutorials-main

# Run the app
python app.py
```

## 💡 Usage

1.  **First Run**: The app will scan the `data/` folder, process all documents, generate embeddings, and build the FAISS vector index. This might take a few minutes depending on the size of your files (e.g., 10 PDFs = ~3 minutes).
2.  **Subsequent Runs**: The app will load the existing index instantly (~50ms).
3.  **Auto-Rebuild**: If you add/modify files in the `data/` folder, the app automatically detects changes and rebuilds the vector store.
4.  **Querying**: Modify the `query` variable in `app.py` to ask different questions about your documents.

### Example Queries:
```python
query = "What are the main topics covered in cloud computing?"
query = "Explain the attention mechanism in transformers"
query = "Summarize Chapter 3 in 3 bullet points"
query = "Who are the authors of this book?"
```

## 📊 Performance

- **Document Loading**: ~1-2s per PDF
- **Embedding Generation**: ~0.5s per 1000 chunks
- **Vector Store Build**: ~2-3s for 10 chunks
- **Query Response Time**: ~2-3s end-to-end
- **FAISS Search**: <10ms
- **Supports**: 4000+ document chunks efficiently

## 🔧 Advanced Features

### Manual Vector Store Rebuild
If you need to force a rebuild (e.g., changed chunking strategy):
```powershell
Remove-Item -Path "faiss_store" -Recurse -Force
python app.py
```

### Supported Document Formats
- 📄 PDF (`.pdf`)
- 📝 Text (`.txt`)
- 📊 CSV (`.csv`)
- 📈 Excel (`.xlsx`)
- 📋 Word (`.docx`)
- 🔢 JSON (`.json`)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
