import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_NAME: str
    DB_PORT: int
    DB_HOST: str
    DB_USER: str
    DB_PASS: str


    @property
    def BASE_DIR(self):
        base_dir = Path(__file__).parent.parent.parent
        return str(base_dir)
    
    @property
    def BACKEND_DIR(self):
        return os.path.join(self.BASE_DIR, "backend")
    
    @property
    def FRONTEND_DIR(self):
        return os.path.join(self.BASE_DIR, "frontend")
    
    @property
    def STATIC_DIR(self):
        return os.path.join(self.FRONTEND_DIR, "static")
    
    @property
    def DB_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()