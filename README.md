# Local AI-Powered Notes Application

A FastAPI-based notes application with sentiment analysis.

## Features
- Secure API with API Key Authentication 
- Create and fetch notes
- Sentiment analysis on notes
- SQLite database
- Dockerized application

## Installation

### 1. Clone the Repository

git clone https://github.com/yourusername/ai-notes-app.git
cd ai-notes-app/backend

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Run the Server

uvicorn app.main:app --reload

### 4. Run Tests

cd backend
pytest tests/test_auth.py

# Docker Setup

docker build -t ai-notes-app .
docker run -d -p 8000:8000 ai-notes-app

# API Endpoints

Method	Endpoint	Description
POST	/notes/	Create a new note
GET	/notes/	Get all notes
GET	/notes/{id}/analyze	Analyze sentiment

# License - MIT - 0.1