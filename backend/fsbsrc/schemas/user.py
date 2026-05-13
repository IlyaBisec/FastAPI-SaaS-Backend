# Task database model.
# Represents tasks inside a project.
# Supports status, priority, assignment.
# 13.05.2026 (c) ilya_bisec

from pydantic import BaseModel
from pydantic import EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str

    model_config = {
        "from_attributes": True
    }