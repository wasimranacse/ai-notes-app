from pydantic import BaseModel, Field
# from typing import List

class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, description="Title cannot be empty")
    content: str = Field(..., min_length=10, description="Content must be at least 10 characters long")

class NoteResponse(NoteCreate):
    id: int  # Include id in the response

    class Config:
        orm_mode = True  # Allows ORM models to be converted to Pydantic models
    
