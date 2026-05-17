# User service.
# Contains business logic for users.
# 16.05.2026 (c) ilya_bisec

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fsbsrc.models.user import User


class UserService:

    @staticmethod
    async def get_all_users(db: AsyncSession):
        result = await db.execute(
            select(User)
        )

        return result.scalars().all()