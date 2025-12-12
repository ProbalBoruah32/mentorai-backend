
🚀 MentorAI Backend — Whisper ASR + AI Scoring Engine









This repository contains the core AI engine for MentorAI, including:

Whisper-based speech-to-text

Audio/video file processing

Segment-wise transcription

AI scoring logic (0–10 scale)

REST API endpoints for web + Android app

📁 Repository Structure
mentorai-backend/

│── server.js

│── package.json

│── .env (create this)

│── /uploads

│── /routes

│── /models

└── Dockerfile

⚙️ 1. Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/ProbalBoruah32/mentorai-backend.git
cd mentorai-backend

2️⃣ Install Dependencies
npm install


This installs:

express

multer

axios

whisper API model handler

cors

dotenv

3️⃣ Environment Variables

Create a .env file:

PORT=5000
HF_TOKEN=your_huggingface_token
HF_MODEL=openai/whisper-small


Generate token here:
👉 https://huggingface.co/settings/tokens

4️⃣ Run Backend Locally
node server.js


If successful, you'll see:

Backend running on port 5000


API will be available at:

http://localhost:5000

☁️ 2. Deployment (Hugging Face Spaces)

This backend supports Docker deployment, making it compatible with Hugging Face Spaces.

Dockerfile (already included)
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 7860
CMD ["node", "server.js"]


Make sure server.js contains:

const PORT = process.env.PORT || 7860;

Deploy Steps
git init
git remote add origin https://huggingface.co/spaces/<yourname>/mentorai-backend
git add .
git commit -m "Deploy MentorAI Backend"
git push origin main


Your public backend will be at:

https://<yourname>-mentorai-backend.hf.space

🔌 API Endpoints
Endpoint	Method	Purpose
/asr	POST	Speech-to-text using Whisper
/upload-and-score	POST	Upload → Transcribe → Score
/translate	POST	Language translation
/health	GET	Server status
🧪 Testing

Use Postman or frontend integration.

📝 Credits


Part of the full MentorAI Communication Assessment System
