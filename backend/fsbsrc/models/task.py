# Task database model.
# Represents tasks inside a project.
# Supports status, priority, assignment.
# 13.05.2026 (c)

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from fsbsrc.core.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(255))

    status: Mapped[str] = mapped_column(default="todo")

    priority: Mapped[str] = mapped_column(default="medium")

    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))

    assigned_to: Mapped[int] = mapped_column(ForeignKey("users.id"))