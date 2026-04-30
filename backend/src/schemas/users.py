from pydantic import BaseModel, Field, EmailStr


class UserRequestAdd(BaseModel):
    login: str
    email: EmailStr | None = None
    password: str


class UserAdd(BaseModel):
    login: str
    email: EmailStr
    hashed_password: str


class User(UserAdd):
    id: int


class UserHashedPassword(User):
    hashed_password: str