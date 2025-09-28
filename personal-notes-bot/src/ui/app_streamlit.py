# src/ui/app_streamlit.py
import streamlit as st
import os
import tempfile
from src.ingest.ingest_service import ingest_files
from src.retrieval.qa import get_answer
from src import config
import logging

logger = logging.getLogger(__name__)

st.set_page_config(page_title="Personal Notes Q&A", layout="centered")
st.title("Personal Notes Q&A Bot (Local - HF models)")

with st.expander("Instructions"):
    st.write(
        """
        1. Upload PDF / DOCX / TXT files and click "Index uploaded files".\n
        2. Ask questions about your notes below.\n
        Notes: This app uses local Hugging Face embedding and LLM models by default.
        The first run will download models and may take time.
        """
    )

uploaded_files = st.file_uploader("Upload files (PDF, DOCX, TXT)", accept_multiple_files=True, type=["pdf", "docx", "txt", "md"])

if st.button("Index uploaded files"):
    if not uploaded_files:
        st.warning("Please upload one or more files to index.")
    else:
        tmpdir = tempfile.mkdtemp(prefix="pnq_")
        file_paths = []
        for up in uploaded_files:
            fp = os.path.join(tmpdir, up.name)
            with open(fp, "wb") as f:
                f.write(up.getbuffer())
            file_paths.append(fp)
        with st.spinner("Indexing... this may take a moment"):
            ingest_files(file_paths, persist_dir=config.CHROMA_PERSIST_DIR)
        st.success("Indexing finished!")

st.markdown("---")
question = st.text_input("Ask a question about your indexed notes")
if st.button("Get answer") and question:
    with st.spinner("Fetching answer..."):
        resp = get_answer(question)
        st.subheader("Answer")
        st.write(resp["answer"])
        st.subheader("Sources")
        for i, s in enumerate(resp["sources"]):
            st.markdown(f"**Source {i+1}** — metadata: `{s.get('metadata')}`")
            st.text(s.get("snippet"))
