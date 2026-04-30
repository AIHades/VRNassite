import os
import jwt

from fastapi import APIRouter, Depends, Form, HTTPException, status

from fastapi.responses import FileResponse
from pwdlib import PasswordHash
from pydantic import EmailStr
from sqlalchemy import select

from src.services.auth import AuthService
from src.models.users import UsersModel
from src.schemas.users import UserAdd, UserHashedPassword, UserRequestAdd

from src.config import settings

from src.database import async_session_maker


router = APIRouter(prefix="/auth", tags=["Авторизация и аутентификация"])


@router.get("/register")
async def redirection_register():
    file_register_path = os.path.join(settings.FRONTEND_DIR, "register/register.html")
    return FileResponse(file_register_path)


@router.get("/login")
async def redirection_login():
    file_login_path = os.path.join(settings.FRONTEND_DIR, "login/login.html")
    return FileResponse(file_login_path)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(    
    username: str = Form(...),
    email: EmailStr = Form(...),
    password: str = Form(...)
):
    new_hash_pass = AuthService().hash_password(password)

    userdata = UserRequestAdd(login=username, email=email, password=new_hash_pass)

    async with async_session_maker() as session:
        query = select(UsersModel).where((UsersModel.login == userdata.login) | (UsersModel.email == userdata.email))
        login = await session.execute(query)

        if login.scalar_one_or_none():
            raise HTTPException(status_code=400, detail="User already exists")
    
        new_user = UsersModel(login = userdata.login, password = new_hash_pass, email = userdata.email, is_admin = False)
    
        session.add(new_user)
        await session.commit()

    return {"status": "ok"}


@router.get("/all_users")
async def get_all_users():
    async with async_session_maker() as session:
        query = select(UsersModel)
        res = await session.execute(query)
        data = res.scalars().all()
        return data


@router.post("/login")
async def login_user(    
    username: str = Form(...),
    email: EmailStr | None = Form(None),
    password: str = Form(...)
):
    userdata = UserRequestAdd(login=username, email= email, password=password)

    async with async_session_maker() as session:
        
        query = select(UsersModel).where((UsersModel.login == userdata.login) | (UsersModel.email == userdata.login))
        res = await session.execute(query)
        user = res.scalar_one_or_none()

        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        
        user_validated = UserHashedPassword(login=user.login, email=user.email, hashed_password=user.password, id= user.id)

        if not AuthService().verify_password(userdata.password, user_validated.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid password")

        access_token = AuthService().create_access_token({"user_id": user_validated.id})

        return {"access_token": access_token}