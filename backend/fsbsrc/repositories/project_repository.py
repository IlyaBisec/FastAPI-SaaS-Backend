# Project repository layer.
# Handles direct database queries for Project model.
# 16.05.2026 (c) ilya_bisec

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fsbsrc.models.project import Project


class ProjectRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        result = await self.db.execute(
            select(Project)
        )

        return result.scalars().all()

    async def create(self, project: Project):
        self.db.add(project)

        await self.db.commit()

        await self.db.refresh(project)

        return project