# src/mcp/router.py
from fastapi import FastAPI, APIRouter, HTTPException
from typing import List
from src.mcp.schemas import DocumentItem, QueryRequest, QueryResponse
from src.ingest.chunker import chunk_text
from src.vectordb.chroma_adapter import ChromaAdapter
from src.retrieval.qa import get_answer
from src import config
import logging

logger = logging.getLogger(__name__)

app = FastAPI(title="MCP - Personal Notes Q&A", version="0.1")
router = APIRouter(prefix="/mcp/v1", tags=["mcp"])

@router.post("/documents", status_code=201)
def add_documents(items: List[DocumentItem]):
    adapter = ChromaAdapter(persist_directory=config.CHROMA_PERSIST_DIR, collection_name="personal_notes")
    docs_to_add = []
    for item in items:
        text = item.text or ""
        chunks = chunk_text(text, chunk_size=config.CHUNK_SIZE, overlap=config.CHUNK_OVERLAP)
        for chunk_text_str, chunk_meta in chunks:
            metadata = dict(chunk_meta)
            metadata.update({"source": item.source or item.title or "mcp_upload"})
            if item.metadata:
                metadata.update(item.metadata)
            docs_to_add.append({"text": chunk_text_str, "metadata": metadata})
    if docs_to_add:
        adapter.add_documents(docs_to_add)
        adapter.persist()
    return {"added": len(docs_to_add)}

@router.post("/query", response_model=QueryResponse)
def query(req: QueryRequest):
    try:
        resp = get_answer(req.query, k=req.k)
        return QueryResponse(answer=resp["answer"], sources=resp["sources"])
    except Exception as e:
        logger.exception("Query failed: %s", e)
        raise HTTPException(status_code=500, detail=str(e))

app.include_router(router)
