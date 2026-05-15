# User repository layer.
# Handles direct database queries for User model.
# 13.05.2026 (c) ilya_bisec

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fsbsrc.models.user import User


class UserRepository:
    """
    Handles user database operations.
    """

    def init(self, db: AsyncSession):
        self.db = db

    async def get_by_email(self, email: str):
        query = select(User).where(User.email == email)

        result = await self.db.execute(query)

        return result.scalar_one_or_none()

    async def create(self, user: User):
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)

        return user