from models.post import Post as PostEntity
from schemas.post import CreatePost
from sqlalchemy.orm import Session


def get_post(db: Session, post_id: int):
    return db.query(PostEntity).filter(PostEntity.id == post_id).first()


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PostEntity).offset(skip).limit(limit).all()

def create_post(db: Session, create_post: CreatePost):
    db_post = PostEntity(id= create_post.id, title=create_post.title, content=create_post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post