# Task schemas.
# Defines request/response models for tasks.
# 16.05.2026 (c) ilya_bisec

from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    priority: str = "medium"


class TaskResponse(BaseModel):
    id: int
    title: str
    status: str
    priority: str

    class Config:
        from_attributes = True