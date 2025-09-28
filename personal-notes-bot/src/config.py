# src/config.py
import os
from dotenv import load_dotenv

load_dotenv()

CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./chroma_db")
VECTOR_DB = os.getenv("VECTOR_DB", "chroma")

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))
TOP_K = int(os.getenv("TOP_K", "4"))

HF_EMBEDDING_MODEL = os.getenv("HF_EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
HF_LLM_MODEL = os.getenv("HF_LLM_MODEL", "google/flan-t5-base")
HF_LLM_MAX_TOKENS = int(os.getenv("HF_LLM_MAX_TOKENS", "256"))
