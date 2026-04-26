from pydantic import BaseModel, Field, EmailStr


class UserRequestAdd(BaseModel):
    login: str
    email: EmailStr
    password: str


class UserAdd(BaseModel):
    login: str
    email: EmailStr
    hashed_password: str


class User(UserAdd):
    id: int