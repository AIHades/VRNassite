import sys
import os

import uvicorn

from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.routers.auth import router as auth_router

from src.config import settings


app = FastAPI()
app.include_router(auth_router)
app.mount("/static", StaticFiles(directory=settings.STATIC_DIR, html=True), name="static")


@app.get("/")
async def homepage():
    file_homepage_path = os.path.join(settings.FRONTEND_DIR, "index.html")
    return FileResponse(file_homepage_path)


@app.get("/aboutUs")
async def aboutUs():
    file_aboutUs_path = os.path.join(settings.FRONTEND_DIR, "aboutUs/aboutUs.html")
    return FileResponse(file_aboutUs_path)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
