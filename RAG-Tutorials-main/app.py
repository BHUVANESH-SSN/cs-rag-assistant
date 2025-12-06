from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

import os

# Example usage
if __name__ == "__main__":
    # Get the absolute path to the data folder (relative to this script)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "../data")
    
    docs = load_all_documents(data_dir)
    store = FaissVectorStore("faiss_store")
    store.build_from_documents(docs)
    store.load()
    
    rag_search = RAGSearch()
    query = "What are the main topics in the provided documents?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)
