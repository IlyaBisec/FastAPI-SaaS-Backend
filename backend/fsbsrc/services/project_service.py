# Project service.
# Contains business logic for projects.
# 16.05.2026 (c) ilya_bisec

from sqlalchemy.ext.asyncio import AsyncSession

from fsbsrc.models.project import Project
from fsbsrc.repositories.project_repository import ProjectRepository


class ProjectService:

    @staticmethod
    async def create_project(
        db: AsyncSession,
        title: str,
        description: str,
        owner_id: int,
    ):
        repo = ProjectRepository(db)

        project = Project(
            title=title,
            description=description,
            owner_id=owner_id,
        )

        return await repo.create(project)

    @staticmethod
    async def get_projects(db: AsyncSession):
        repo = ProjectRepository(db)

        return await repo.get_all()