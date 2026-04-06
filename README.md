
#  Document QnA with LLaVA  

# 📄 AI Document Question Answering System (PDF + DOCX)

This project is an offline AI-powered system that extracts text from PDF and DOCX files, processes the content into manageable chunks, and answers user queries based on the document content using the LLaVA model (via Ollama).

The system works completely offline once the required models are downloaded, making it fast, secure, and independent of external APIs.

---

## 🚀 Features

- 📄 Extract text from PDF files  
- 📝 Extract text from DOCX files  
- ✂️ Smart text chunking for efficient processing  
- 🔍 Finds the most relevant content based on user query  
- 🤖 Uses LLaVA model locally via Ollama  
- 🌐 No API required  
- 🔒 Works fully offline  

---

## 🧠 How It Works

1. The system extracts text from PDF and DOCX files  
2. The text is divided into smaller chunks (for better processing)  
3. When a user asks a question:
   - The system finds the most relevant chunk  
   - Sends it to the LLaVA model  
4. The model generates a context-based answer  

---

## 🛠️ Tech Stack

- Python  
- PyPDF2  
- python-docx  
- Ollama (LLaVA model)  

---

## ⚙️ Requirements

- Python 3.x  
- Ollama installed  
- LLaVA model downloaded  

---

## ▶️ Usage

1. Place your PDF and DOCX files in the project directory  
2. Run the script:

```bash
python main.py
