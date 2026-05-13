# Auth Service -
# 13.05.2026 (c) ilya_bisec

from app.core.security import create_access_token
from app.core.security import hash_password
from app.core.security import verify_password
from app.models.user import User
from app.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def register(self, email: str, password: str):
        user = User(
            email=email,
            hashed_password=hash_password(password),
        )

        return await self.repository.create(user)

    async def login(self, email: str, password: str):
        user = await self.repository.get_by_email(email)

        if not user:
            return None

        if not verify_password(password, user.hashed_password):
            return None

        token = create_access_token(
            {
                "sub": str(user.id),
                "role": user.role,
            }
        )

        return token