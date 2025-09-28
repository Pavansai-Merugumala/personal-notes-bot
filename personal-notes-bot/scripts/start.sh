#!/usr/bin/env bash
# Activate venv if present
if [ -f ".venv/bin/activate" ]; then
  source .venv/bin/activate
fi

# Run Streamlit UI
streamlit run src/ui/app_streamlit.py
