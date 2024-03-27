import controller as c
import schema as s
from config import Settings, get_settings
from database import get_db
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["Authentication"])


@auth_router.post(
    "/signup",
    status_code=status.HTTP_201_CREATED,
    response_model=s.Token,
)
def signup(
    user_credentials: s.SignUpCredentials,
    db: Session = Depends(get_db),
    settings: Settings = Depends(get_settings),
):
    return c.signup(user_credentials, db, settings)


@auth_router.post("/login", status_code=status.HTTP_200_OK, response_model=s.Token)
def login(
    user_credentials: s.LoginCredentials,
    db: Session = Depends(get_db),
    settings: Settings = Depends(get_settings),
):
    return c.login(user_credentials, db, settings)
