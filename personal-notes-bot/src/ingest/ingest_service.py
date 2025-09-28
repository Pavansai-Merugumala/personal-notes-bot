# src/ingest/ingest_service.py
from typing import List
import logging
from src.ingest.parser import parse_file
from src.ingest.chunker import chunk_text
from src.vectordb.chroma_adapter import ChromaAdapter
from src import config

logger = logging.getLogger(__name__)

def ingest_files(file_paths: List[str], persist_dir: str = None):
    if persist_dir is None:
        persist_dir = config.CHROMA_PERSIST_DIR

    adapter = ChromaAdapter(persist_directory=persist_dir, collection_name="personal_notes")

    for fp in file_paths:
        logger.info("Parsing file %s", fp)
        text, meta = parse_file(fp)
        if not text:
            logger.warning("No text extracted from %s", fp)
            continue

        chunks = chunk_text(text, chunk_size=config.CHUNK_SIZE, overlap=config.CHUNK_OVERLAP)
        docs = []
        for chunk_text_str, chunk_meta in chunks:
            metadata = dict(meta)
            metadata.update(chunk_meta)
            docs.append({"text": chunk_text_str, "metadata": metadata})
        if docs:
            logger.info("Adding %d docs from file %s", len(docs), fp)
            adapter.add_documents(docs)
    adapter.persist()
    logger.info("Ingest complete.")
    return True
