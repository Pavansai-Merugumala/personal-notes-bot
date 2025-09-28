# src/retrieval/qa.py
from langchain.chains import RetrievalQA
from langchain import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from src.retrieval.retriever import get_retriever
from src import config
import logging

logger = logging.getLogger(__name__)

# Prepare HF pipeline and wrap in LangChain's HuggingFacePipeline
def _build_local_llm():
    model_name = config.HF_LLM_MODEL
    logger.info("Loading HF LLM model: %s (this may take a while the first time)", model_name)
    # For seq2seq models like Flan-T5 use text2text-generation
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    hf_pipe = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=config.HF_LLM_MAX_TOKENS,
        truncation=True
    )
    return HuggingFacePipeline(pipeline=hf_pipe)

_llm_instance = None
def get_llm():
    global _llm_instance
    if _llm_instance is None:
        _llm_instance = _build_local_llm()
    return _llm_instance

def get_answer(question: str, k: int = None):
    retriever = get_retriever(k=k)
    llm = get_llm()
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    logger.info("Running RAG for question: %s", question)
    result = qa({"query": question})
    # langchain versions vary in key names
    answer = result.get("result") or result.get("output_text") or str(result)
    # get relevant documents for sources (retriever interface may vary)
    try:
        docs = retriever.get_relevant_documents(question)
    except Exception:
        docs = []
    sources = []
    for d in docs[: config.TOP_K]:
        meta = d.metadata if hasattr(d, "metadata") else {}
        snippet = (d.page_content[:400] + "...") if len(d.page_content) > 400 else d.page_content
        sources.append({"snippet": snippet, "metadata": meta})
    return {"answer": answer, "sources": sources}
