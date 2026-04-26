import os

from fastapi import APIRouter, Form, HTTPException

from fastapi.responses import FileResponse
from pwdlib import PasswordHash
from pydantic import EmailStr

from src.schemas.users import UserAdd, UserRequestAdd

from src.config import settings


router = APIRouter(prefix="/auth", tags=["Авторизация и аутентификация"])

test_db = []


@router.get("/register")
async def redirection_login():
    file_login_path = os.path.join(settings.FRONTEND_DIR, "register/register.html")
    return FileResponse(file_login_path)


@router.get("/login")
async def redirection_login():
    file_login_path = os.path.join(settings.FRONTEND_DIR, "login/login.html")
    return FileResponse(file_login_path)


password_hash = PasswordHash.recommended()


@router.post("/register")
def register_user(username: str = Form(), email: EmailStr = Form(), password: str =Form()):
    new_hash_pass = password_hash.hash(password)
    user = {"username":username, "email": email,"hash_pass" : new_hash_pass}
    test_db.append(user)
    return test_db


@router.post("/login")
def login_user(username: str = Form(), email: str | None = Form(None), password: str = Form()):
    user = ""

    for datauser in test_db:
        if datauser["username"] == username: 
            user = username
            break

    if password_hash.verify(password, datauser["hash_pass"]):
        if user == "admin": return "admin"
        else: return "user"

    raise HTTPException(status_code=401, detail="неверный логин или пароль")



# password_hash = PasswordHash.recommended()


#для базы данных 
# @router.post("/register")
# async def register_user(data: UserRequestAdd) ->UserAdd:
#     new_hash_pass = password_hash.hash(data.password)
#     new_user_data = UserAdd(login=data.login, email = data.email, hashed_password=new_hash_pass)
#     return new_user_data