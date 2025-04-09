from pydantic import BaseModel, Field, ConfigDict

class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, description="Title cannot be empty")
    content: str = Field(..., min_length=10, description="Content must be at least 10 characters long")

class NoteResponse(NoteCreate):
    id: int  # Include id in the response

    model_config = ConfigDict(from_attributes=True)

    
