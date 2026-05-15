# Authentication service.
# Contains business logic for:
# - registration
# - login
# - password validation
# - token creation
# 13.05.2026 (c) ilya_bisec

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from fsbsrc.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)

from fsbsrc.models.user import User
from fsbsrc.repositories.user_repository import UserRepository
from fsbsrc.schemas.auth import RegisterRequest, LoginRequest


class AuthService:
    """
    Handles authentication business logic.
    """

    def init(self, db: AsyncSession):
        self.user_repo = UserRepository(db)

    async def register(self, data: RegisterRequest):
        existing_user = await self.user_repo.get_by_email(data.email)

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="User already exists",
            )

        user = User(
            email=data.email,
            username=data.username,
            hashed_password=hash_password(data.password),
        )

        return await self.user_repo.create(user)

    async def login(self, data: LoginRequest):
        user = await self.user_repo.get_by_email(data.email)

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials",
            )

        if not verify_password(
            data.password,
            user.hashed_password,
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials",
            )

        token = create_access_token({
            "sub": user.email,
            "role": user.role,
        })

        return {
            "access_token": token,
            "token_type": "bearer",
        }