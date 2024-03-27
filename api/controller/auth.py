import model as m
import schema as s
import sqlalchemy as sa

from config import Settings
from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session


def signup(user_credentials: s.SignUpCredentials, db: Session, settings: Settings):
    if db.scalar(sa.exists().where(m.User.email == user_credentials.email)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists"
        )

    user = m.User(email=user_credentials.email, password=user_credentials.password)

    db.add(user)
    db.commit()

    return s.SignUpCredentialsOut(email=user.email)


def login(user_credentials: s.LoginCredentials, db: Session, settings: Settings):
    user: m.User | None = db.scalar(
        sa.exists().where(m.User.email == user_credentials.email)
    )

    if not user or not user.check_password(user_credentials.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    return s.LoginCredentialsOut(email=user.email)
