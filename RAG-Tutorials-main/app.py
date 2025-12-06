import os
print("--- RAG Application Initializing (Imports may take a moment) ---")

import os
os.environ['TORCH_DYNAMO_DISABLE'] = '1'

from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

# Example usage
if __name__ == "__main__":
    print("--- RAG Application Starting Execution ---")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "../data")
    
    store = FaissVectorStore("faiss_store")
    
    if not os.path.exists("faiss_store/faiss.index"):
        print("[INFO] Vector store not found. Building from documents...")
        docs = load_all_documents(data_dir)
        store.build_from_documents(docs)
    else:
        print("[INFO] Loading existing vector store...")
        store.load()
    
    rag_search = RAGSearch()
    query = "who is the authors of the book cloud computing name them?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)
