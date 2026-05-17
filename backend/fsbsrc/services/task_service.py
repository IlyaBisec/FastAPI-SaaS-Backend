# Task service.
# Contains business logic for tasks.
# 16.05.2026 (c) ilya_bisec

from sqlalchemy.ext.asyncio import AsyncSession

from fsbsrc.models.task import Task
from fsbsrc.repositories.task_repository import TaskRepository


class TaskService:

    @staticmethod
    async def create_task(
        db: AsyncSession,
        title: str,
        project_id: int,
        assigned_to: int,
    ):
        repo = TaskRepository(db)

        task = Task(
            title=title,
            project_id=project_id,
            assigned_to=assigned_to,
        )

        return await repo.create(task)

    @staticmethod
    async def get_tasks(db: AsyncSession):
        repo = TaskRepository(db)

        return await repo.get_all()