from typing import List, Union

from crud.base import create_post as createPost
from db.base import SessionLocal
from fastapi import APIRouter, Depends, HTTPException, Path, Query
from schemas import CreatePost, Post
from sqlalchemy.orm import Session
from typing_extensions import Annotated

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.get(path='', response_model=List[Post])
def get_posts():
    post_1 = Post(id=1, title='title1', content='content111111')
    post_2 = Post(id=2, title='title2', content='content2222')
    dummy_posts = []
    dummy_posts.append(post_1)
    dummy_posts.append(post_2)
    return dummy_posts



@router.get(path='/{post_id}', response_model=Post)
def get_post_by_id(post_id:int = Path(title="The Id of the post to get")):
    post_1 = Post(id=1, title='title1', content='content111111')
    post_2 = Post(id=2, title='title2', content='content2222')
    dummy_posts = []
    dummy_posts.append(post_1)
    dummy_posts.append(post_2)
    for post in dummy_posts:
        if post.id == post_id:
            return post
    return None


@router.post(path='')
def create_post(create_post: CreatePost, db: Session = Depends(get_db)):
    return createPost(db, create_post=create_post)