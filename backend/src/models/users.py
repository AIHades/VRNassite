from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from src.database import Base


class UsersModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))
    is_admin: Mapped[bool]