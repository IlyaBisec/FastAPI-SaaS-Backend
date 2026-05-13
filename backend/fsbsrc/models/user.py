# User database model.
# Represents users in the system including:
# - authentication data
# - roles
# - account status
# 13.05.2026 (c) ilya_bisec

from datetime import datetime
from enum import Enum

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from fsbsrc.core.database import Base

class UserRole(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True,
    )

    hashed_password: Mapped[str]

    role: Mapped[str] = mapped_column(default=UserRole.USER)

    is_active: Mapped[bool] = mapped_column(default=True)

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)