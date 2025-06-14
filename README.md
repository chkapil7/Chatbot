
# 🤖 RAG Chatbot

A full-stack AI Chatbot with support for **Google OAuth login**, **Gemini/Ollama model selection**, **Markdown rendering**, **chat history persistence**, and a responsive **React + Tailwind CSS** frontend powered by a FastAPI backend.

---

## 🚀 Features

- 🔐 Google OAuth 2.0 Authentication
- 🧠 Choose between Gemini or Ollama models
- 📝 Markdown rendering with code highlighting
- 💾 Persistent chat history using MongoDB
- 🌙 Dark/Light mode switch
- ⌛ Typing indicators
- 🕒 Timestamped messages
- 📱 Fully responsive design with Tailwind CSS

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
```

### 2. Backend Setup (FASTAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file in the `backend/` directory:

```env
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/chatbot
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GEMINI_API_KEY=your-gemini-api-key
OLLAMA_ENDPOINT=http://localhost:11434
```

### 4. Run Backend Server

```bash
uvicorn main:app --reload
```

### 5. Frontend Setup (React + Vite + Tailwind CSS)

```bash
cd ../frontend
npm install
npm install axios react-router-dom
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
npm run dev
```

Visit: [http://localhost:5173](http://localhost:5173)

---

## 🧪 How to Use

1. Start the backend using `uvicorn`.
2. Start the frontend using `npm run dev`.
3. Log in with Google or Local Database Authentication.
4. Select your preferred model (Gemini or Ollama).
5. Start chatting and view your message history!

---

## 🧑‍💻 Contributors

| Name            | Contribution Area                          |
|-----------------|--------------------------------------------|
| [CH Kapil Anirudh](https://github.com/chkapil7?tab=repositories)    | Google Auth, Chat UI, FastAPI APIs, MongoDB Setup, Chat History Storage         |
| [Manogna VL](https://github.com/manogna2508)             |  UI, Model Selector, Markdown Renderer, Ollama & Gemini API Integration, Embedding      |

---

## 🧱 Tech Stack

- **Frontend**: React, Vite, Tailwind CSS, ShadCN UI
- **Backend**: FastAPI, Python
- **Database**: MongoDB (using Motor)
- **Authentication**: Local Authentication (as of now)
- **AI Models**: Gemini Pro, Ollama
- **Embedding & Retrieval**: Sentence Transformers, FAISS

---

## 🔮 Future Enhancements

- 🎙️ Voice-based input
- 🗂️ Multi-session chat history
- 🔍 Full-text search across chats
- 📱 Progressive Web App (PWA)
- 🧠 Knowledge Graph integration
- 🧾 Admin panel & analytics dashboard
- 🔏 Google OAuth 2.0

---

## 📄 License

This project is licensed under the MIT License.
