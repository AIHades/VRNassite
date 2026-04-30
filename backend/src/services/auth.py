from datetime import datetime, timedelta, timezone

import jwt

from pwdlib import PasswordHash

from src.schemas.users import UserHashedPassword
from src.config import settings

class AuthService:
    def __init__(self):
        self.password_hash = PasswordHash.recommended()


    def verify_password(self, plain_password, hashed_password):
        return self.password_hash.verify(plain_password, hashed_password)
    

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return encoded_jwt
    

    def hash_password(self, password):
        return self.password_hash.hash(password)