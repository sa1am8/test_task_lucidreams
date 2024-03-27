import model as m
import schema as s
import sqlalchemy as sa
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


def create_post(
    post_data: s.PostCreate, current_user: m.User, db: Session
) -> s.PostOut:
    post = m.Post(
        title=post_data.title,
        content=post_data.content,
        author_id=current_user.id,
    )

    db.add(post)
    db.commit()

    return s.PostOut.model_validate(post)


def get_posts(user_id: int, db: Session) -> s.PostsOut:
    posts = db.scalars(sa.select(m.Post)).where(m.Post.author_id == user_id).all()

    return s.PostsOut(posts=[s.PostOut.model_validate(post) for post in posts])


def delete_post(post_id: int, current_user: m.User, db: Session):
    post = db.scalar(sa.select(m.Post).where(m.Post.id == post_id))

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )

    if post.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="You are not the author"
        )

    db.delete(post)
    db.commit()
