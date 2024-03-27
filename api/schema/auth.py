from pydantic import BaseModel


class SignUpCredentials(BaseModel):
    email: str
    password: str


class SignUpCredentialsOut(BaseModel):
    email: str


class LoginCredentials(BaseModel):
    email: str
    password: str


class LoginCredentialsOut(BaseModel):
    email: str


class Token(BaseModel):
    access_token: str
    token_type: str
