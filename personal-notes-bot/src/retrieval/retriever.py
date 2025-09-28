# src/retrieval/retriever.py
from src.vectordb.chroma_adapter import ChromaAdapter
from src import config

def get_retriever(persist_dir: str = None, k: int = None):
    adapter = ChromaAdapter(persist_directory=persist_dir or config.CHROMA_PERSIST_DIR, collection_name="personal_notes")
    search_kwargs = {"k": (k or config.TOP_K)}
    return adapter.as_retriever(search_kwargs=search_kwargs)
