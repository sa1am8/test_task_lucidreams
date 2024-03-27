import controller as c
import model as m
import schema as s
from cachetools import TTLCache, cached
from database import get_db
from fastapi import APIRouter, Depends, status
from schema import get_current_user
from sqlalchemy.orm import Session

cache = TTLCache(maxsize=100, ttl=300)  # 5 minutes

post_router = APIRouter(prefix="/posts", tags=["Posts"])


@post_router.get(
    "/{user_id}", response_model=s.PostsOut, status_code=status.HTTP_200_OK
)
@cached(cache)
def get_user_posts(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: m.User = Depends(get_current_user),
):
    return c.get_posts(user_id, db)


@post_router.post("", status_code=status.HTTP_201_CREATED, response_model=s.PostOut)
def create_post(
    data: s.PostCreate,
    db: Session = Depends(get_db),
    current_user: m.User = Depends(get_current_user),
):
    return c.create_post(data, current_user, db)


@post_router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: m.User = Depends(get_current_user),
):
    c.delete_post(post_id, current_user, db)
