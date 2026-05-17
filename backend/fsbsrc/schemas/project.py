# Project schemas.
# Defines request/response models for projects.
# 16.05.2026 (c) ilya_bisec

from pydantic import BaseModel


class ProjectCreate(BaseModel):
    title: str
    description: str


class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        from_attributes = True