# Authentication service.
# Contains business logic for:
# - registration
# - login
# - password validation
# - token creation
# 13.05.2026 (c) ilya_bisec

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fsbsrc.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from fsbsrc.models.user import User


class AuthService:
    @staticmethod
    async def register(
        db: AsyncSession,
        email: str,
        username: str,
        password: str,
    ):
        user = User(
            email=email,
            username=username,
            hashed_password=hash_password(password),
        )

        db.add(user)

        await db.commit()

        await db.refresh(user)

        return user

    @staticmethod
    async def authenticate(
        db: AsyncSession,
        email: str,
        password: str,
    ):
        result = await db.execute(
            select(User).where(User.email == email)
        )

        user = result.scalar_one_or_none()

        if not user:
            return None

        if not verify_password(password, user.hashed_password):
            return None

        return user

    @staticmethod
    def create_token(user: User):
        return create_access_token({"sub": str(user.id)})