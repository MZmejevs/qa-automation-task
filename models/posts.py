from typing import Optional
from pydantic import BaseModel

class CreatePostModel(BaseModel):
    title: str
    body: str
    userId: int

class UpdatePostModel(BaseModel):
    title: str
    id: Optional[int] = None
    body: Optional[str] = None
    userId: Optional[int] = None

class PostModel(BaseModel):
    userId: int
    id: int
    title: str
    body: str
