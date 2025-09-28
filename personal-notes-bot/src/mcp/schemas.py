# src/mcp/schemas.py
from pydantic import BaseModel
from typing import List, Dict, Optional

class DocumentItem(BaseModel):
    id: Optional[str] = None
    text: str
    title: Optional[str] = None
    source: Optional[str] = None
    tags: Optional[List[str]] = None
    metadata: Optional[Dict] = None

class QueryRequest(BaseModel):
    query: str
    k: Optional[int] = 4
    session_id: Optional[str] = None

class QueryResponse(BaseModel):
    answer: str
    sources: List[Dict]
