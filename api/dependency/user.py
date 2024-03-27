from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session
from sqlalchemy import select

from api.oauth2 import verify_access_token
from api.database import get_db
from api.logger import log
from api.config import get_settings, Settings
import api.model as m
import api.schema as s

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
settings: Settings = get_settings()


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> m.User:
    """Raises an exception if the current user is not authenticated"""
    token: s.TokenData = verify_access_token(token)
    user: m.User | None = db.scalar(select(m.User)).where(m.User.id == token.user_id)
    if not user:
        log(log.INFO, "User wasn`t authorized")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User wasn`t authorized",
        )
    if user.is_deleted:
        log(log.INFO, "User wasn't found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User wasn't found",
        )
    return user
