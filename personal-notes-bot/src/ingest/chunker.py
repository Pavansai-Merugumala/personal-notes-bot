# src/ingest/chunker.py
from typing import List, Tuple
import logging

logger = logging.getLogger(__name__)

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[Tuple[str, dict]]:
    if not text:
        return []
    chunks = []
    start = 0
    length = len(text)
    chunk_id = 0
    while start < length:
        end = min(start + chunk_size, length)
        chunk = text[start:end].strip()
        if chunk:
    
            meta = {"chunk_id": chunk_id, "start": start, "end": end}
            chunks.append((chunk, meta))
            chunk_id += 1
        start += chunk_size - overlap
    logger.info("Created %d chunks", len(chunks))
    return chunks
