
# 🧠 Personal Notes Q&A Bot

A simple yet powerful AI-powered application that lets you **ask questions from your personal notes** — just like chatting with your own knowledge base!

This project demonstrates how to combine **document processing**, **vector embeddings**, and **LLM-powered Q&A** into an interactive web app.

---

## 🚀 Features

- 📁 Upload your personal notes (`.txt`, `.pdf`, `.docx`, etc.)
- 🔍 Automatic text extraction and chunking
- 🧬 Semantic search using embeddings (e.g., OpenAI embeddings + FAISS/Chroma)
- 💬 Ask natural language questions and get accurate answers from your own notes
- ⚡ Built with a lightweight, interactive web interface
- ☁️ Easy to deploy on Streamlit Cloud or locally

---

## 🛠️ Tech Stack

| Component | Technology Used |
|------------|-----------------|
| Frontend | Streamlit |
| Backend | Python |
| Embeddings | OpenAI Embeddings API |
| LLM | GPT Model (via OpenAI API) |
| Vector Store | FAISS / ChromaDB |
| Document Parsing | PyPDF2, docx2txt, and Text handling |

---

## 📂 Project Structure

```

personal-notes-qa-bot/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── utils/
│   ├── text_splitter.py  # Chunking and preprocessing
│   ├── vector_store.py   # Embedding and search logic
│   └── qa_engine.py      # Q&A generation logic
│
├── data/
│   └── sample_notes/     # Example user notes
│
└── README.md

````

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/personal-notes-qa-bot.git
   cd personal-notes-qa-bot
````

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # For macOS/Linux
   venv\Scripts\activate      # For Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your OpenAI API key**

   * Create a `.env` file in the project root and add:

     ```
     OPENAI_API_KEY=your_api_key_here
     ```

5. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## 💡 How It Works

1. **Upload Notes:** The app reads your documents and splits text into manageable chunks.
2. **Create Embeddings:** Each chunk is converted into an embedding vector for semantic search.
3. **Ask a Question:** When you ask something, the app finds the most relevant text pieces.
4. **Generate Answer:** The selected context is sent to the GPT model, which crafts an accurate, concise answer.

---

## 🧩 Example Use Case

| Scenario                   | Description                                                |
| -------------------------- | ---------------------------------------------------------- |
| 🧾 Student Notes           | Upload class notes and instantly clarify concepts          |
| 💼 Work Docs               | Quickly find information from reports or meeting summaries |
| 🧘 Personal Knowledge Base | Chat with your own ideas, saved learnings, or journals     |

---

## 📸 Screenshot (Optional)

*(Add your app screenshot here once deployed)*

```
![App Screenshot](./screenshot.png)
```

---

## 🚀 Future Enhancements

* Support for multiple file uploads at once
* Persistent database for long-term memory
* Chat history and conversation context
* Voice input and text-to-speech answers
* Deployment on Streamlit Cloud or Hugging Face Spaces

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/<your-username>/personal-notes-qa-bot/issues).

---

## 🧑‍💻 Author

**Pavan Sai Merugumala**
📧 [pavansaimerugumala@gmail.com](mailto:pavansaimerugumala@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/pavan-sai-merugumala/) | [GitHub](https://github.com/<your-username>)

---
