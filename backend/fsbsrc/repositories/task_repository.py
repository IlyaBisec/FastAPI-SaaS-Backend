# Task repository layer
# Handles direct database queries for Task model.
# 16.05.2026 (c) ilya_bisec

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fsbsrc.models.task import Task


class TaskRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        result = await self.db.execute(
            select(Task)
        )

        return result.scalars().all()

    async def create(self, task: Task):
        self.db.add(task)

        await self.db.commit()

        await self.db.refresh(task)

        return task