# 📚 Student RAG Assistant

A powerful **Retrieval-Augmented Generation (RAG)** application designed to help students study efficiently. This tool ingests your study materials (PDFs, Textbooks, Notes) and allows you to ask questions, get summaries, and find specific information instantly using AI.

## 🚀 Features

- **Multi-Format Support**: Load PDFs, Text files, CSVs, and more from the `data/` directory.
- **Smart Retrieval**: Uses **FAISS** for fast and accurate vector similarity search.
- **High-Performance LLM**: Powered by **Groq** (using `gemma2-9b-it`) for lightning-fast responses.
- **Local Embeddings**: Uses `SentenceTransformers` to keep embedding generation local and free.
- **Persistent Storage**: Saves your vector index so you don't have to reload documents every time.

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Framework**: [LangChain](https://www.langchain.com/)
- **LLM Provider**: [Groq Cloud](https://groq.com/)
- **Model**: `gemma2-9b-it`
- **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2`
- **Vector Database**: [FAISS](https://github.com/facebookresearch/faiss)
- **Document Parsing**: `PyMuPDF`, `pypdf`

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

1.  **First Run**: The app will scan the `data/` folder, process all documents, and build the FAISS vector index. This might take a moment depending on the size of your files.
2.  **Subsequent Runs**: The app will load the existing index instantly.
3.  **Querying**: Modify the `query` variable in `app.py` to ask different questions about your documents.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
