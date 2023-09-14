from pydantic import BaseModel


class Post(BaseModel):
    id :int
    title :str
    content :str


class CreatePost(BaseModel):
    id: int
    title: str
    content: str