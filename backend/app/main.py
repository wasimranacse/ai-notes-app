from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Note
from schemas import NoteCreate
from typing import List
from schemas import NoteResponse  
from sentiment import analyze_sentiment


app = FastAPI()

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.get("/")
# def welcome_message():
#     return {"message": "Welcome to the Notes AI"}

@app.get("/notes/", response_model=List[NoteResponse])
def get_notes(db: Session = Depends(get_db)):
    notes = db.query(Note).all()
    return notes

@app.post("/notes/")
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    # Create a new note and store it in the database.
    new_note = Note(title=note.title, content=note.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return {"message": "Note created successfully", "note": new_note}

@app.get("/notes/{note_id}/analyze")
def analyze_note_sentiment(note_id: int, db: Session = Depends(get_db)):
    """Fetches a note by ID and analyzes its sentiment."""
    note = db.query(Note).filter(Note.id == note_id).first()
    
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    sentiment = analyze_sentiment(note.content)
    return {"note_id": note.id, "title": note.title, "sentiment": sentiment}


