# Local AI-Powered Notes Application

A FastAPI-based notes application with sentiment analysis.

## Features
- Secure API with API Key Authentication 
- Create notes
- List of all the notes
- Sentiment analysis on notes
- SQLite database - Store all the notes
- Dockerized application 

## Technologies Used

- Python 3.12
- FastAPI
- SQLite Database
- SQLAlchemy
- Pydantic
- Pytest (for testing)

## Prerequisites

1. Python 3.12+
2. MySQL Server
3. Install necessary Python libraries with pip:
4. Docker Desktop
5. Visual Studio Code or any other IDE

## Available Authorizations

X-API-KEY: local123987@1122!

## Installation
```sh
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/ai-notes-app.git
cd ai-notes-app/backend

### 2. Install Dependencies
```sh
pip install -r requirements.txt

### 3. Run the Server
```sh
cd ai-notes-app/backend/app
uvicorn main:app --reload

### 4. Run Tests
```sh
cd backend 
pytest tests/test_auth.py

# Docker Setup
```sh
docker build -t ai-notes-app .
docker run -d -p 8000:8000 ai-notes-app

# API Endpoints

Method	Endpoint	Description
POST	/notes/	Create a new note
GET	/notes/	Get all notes
GET	/notes/{id}/analyze	Analyze sentiment

# License - MIT - 0.1