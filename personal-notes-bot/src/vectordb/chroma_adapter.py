# src/vectordb/chroma_adapter.py
from typing import List, Dict, Optional
import logging
from langchain.docstore.document import Document
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from src import config

logger = logging.getLogger(__name__)

class ChromaAdapter:
    def __init__(self, persist_directory: Optional[str] = None, collection_name: str = "personal_notes"):
        self.persist_directory = persist_directory or config.CHROMA_PERSIST_DIR
        self.collection_name = collection_name
        # Use HuggingFaceEmbeddings (sentence-transformers) locally
        self.embeddings = HuggingFaceEmbeddings(model_name=config.HF_EMBEDDING_MODEL)
        self._db = None

    def _init_db(self):
        if self._db is None:
            logger.info("Initializing Chroma at %s (collection=%s)", self.persist_directory, self.collection_name)
            self._db = Chroma(persist_directory=self.persist_directory, collection_name=self.collection_name, embedding_function=self.embeddings)
        return self._db

    def add_documents(self, docs: List[Dict[str, object]]):
        db = self._init_db()
        lc_docs = [Document(page_content=d["text"], metadata=d.get("metadata")) for d in docs]
        db.add_documents(lc_docs)
        logger.info("Added %d documents to Chroma", len(lc_docs))
        return True

    def persist(self):
        db = self._init_db()
        try:
            db.persist()
            logger.info("Chroma persisted at %s", self.persist_directory)
        except Exception:
            logger.exception("Chroma persist failed (may be ok in some setups)")

    def as_retriever(self, search_kwargs: dict = None):
        db = self._init_db()
        return db.as_retriever(search_kwargs=search_kwargs or {})

    def similarity_search(self, query: str, k: int = 4):
        db = self._init_db()
        return db.similarity_search_with_score(query, k=k)

    def get_collection(self):
        return self._init_db()
