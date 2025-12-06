import os
import shutil
from pathlib import Path
print("--- RAG Application Initializing (Imports may take a moment) ---")

import os
os.environ['TORCH_DYNAMO_DISABLE'] = '1'

from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch


def get_data_modification_time(data_dir):
    """Get the most recent modification time of any file in data directory"""
    data_path = Path(data_dir)
    if not data_path.exists():
        return 0
    
    all_files = list(data_path.glob('**/*.*'))
    if not all_files:
        return 0
    
    return max(f.stat().st_mtime for f in all_files if f.is_file())


if __name__ == "__main__":
    print("--- RAG Application Starting Execution ---")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "../data")
    vector_store_path = "faiss_store"
    rebuild_flag_file = os.path.join(vector_store_path, ".last_build_time")
    
    store = FaissVectorStore(vector_store_path)
    
    # Check if we need to rebuild
    need_rebuild = False
    
    if not os.path.exists(os.path.join(vector_store_path, "faiss.index")):
        print("[INFO] Vector store not found. Building from documents...")
        need_rebuild = True
    else:
        # Check if data folder has been modified since last build
        current_data_time = get_data_modification_time(data_dir)
        
        if os.path.exists(rebuild_flag_file):
            with open(rebuild_flag_file, 'r') as f:
                last_build_time = float(f.read().strip())
            
            if current_data_time > last_build_time:
                print("[INFO] Data folder has been modified. Rebuilding vector store...")
                need_rebuild = True
                # Clear old vector store
                if os.path.exists(vector_store_path):
                    shutil.rmtree(vector_store_path)
                    os.makedirs(vector_store_path, exist_ok=True)
        else:
            print("[INFO] No build timestamp found. Rebuilding vector store...")
            need_rebuild = True
    
    if need_rebuild:
        docs = load_all_documents(data_dir)
        if len(docs) == 0:
            print("[ERROR] No documents found in data folder!")
            exit(1)
        store.build_from_documents(docs)
        # Save the build timestamp
        with open(rebuild_flag_file, 'w') as f:
            f.write(str(get_data_modification_time(data_dir)))
    else:
        print("[INFO] Loading existing vector store (data unchanged)...")
        store.load()
    
    # Pass the existing store to RAGSearch to avoid reloading embedding model
    rag_search = RAGSearch(vectorstore=store)
    query = "What are the main topics covered in the documents?"
    print(f"\n📝 Query: {query}\n")
    summary = rag_search.search_and_summarize(query, top_k=3)
    print(f"\n✅ Answer:\n{summary}\n")
