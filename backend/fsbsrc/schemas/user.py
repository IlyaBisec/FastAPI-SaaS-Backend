# Task database model.
# Represents tasks inside a project.
# Supports status, priority, assignment.
# 13.05.2026 (c) ilya_bisec

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str

    class Config:
        from_attributes = True