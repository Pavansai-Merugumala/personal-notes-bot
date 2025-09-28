# src/logging_config.py
import logging

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    logging.getLogger("pdfminer").setLevel(logging.WARNING)
    logging.getLogger("chromadb").setLevel(logging.WARNING)
