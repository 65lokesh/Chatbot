# 🤖 AI Chatbot using RAG (Retrieval-Augmented Generation)

## 📌 Overview

This project is an AI-powered chatbot built using **Retrieval-Augmented Generation (RAG)**.
It retrieves relevant information from documents and generates accurate, context-aware responses using LLMs.

---

## 🚀 Features

* 🔍 Document-based Question Answering
* 📄 Supports PDF/Text data sources
* 🧠 Context-aware responses using RAG
* ⚡ Fast API backend
* 🔐 Environment-based configuration

---

## 🛠️ Tech Stack

* Python
* Flask / FastAPI
* LangChain
* OpenAI / LLM APIs
* Vector Database (FAISS / Chroma)

---

## 📂 Project Structure

```
Chatbot/
│── Api/
│   ├── app.py
│   ├── client.py
│
│── Rag/
│   ├── simplerag.ipynb
│   ├── Speech.txt
│
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/65lokesh/Chatbot.git
cd Chatbot
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
python Api/app.py
```

---

## 💡 How it Works

1. Load documents (PDF/Text)
2. Convert into embeddings
3. Store in vector database
4. Retrieve relevant chunks
5. Generate response using LLM

---

## 📸 Demo

*Add screenshots or demo link here*

---

## 🧠 Future Improvements

* Add UI (React Chat Interface)
* Multi-document support
* Voice-based chatbot
* Deployment (Render / Railway)

---

## 👨‍💻 Author

**Lokesh Patil**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
