from pydantic import BaseModel

class CommentModel(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str
