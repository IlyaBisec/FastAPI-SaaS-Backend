# Auth API routes.
# Defines HTTP endpoints for:
# - user registration
# - login
# - token generation
# 13.05.2026 (c) ilya_bisec

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from fsbsrc.core.database import get_db
from fsbsrc.schemas.auth import (
    LoginRequest,
    RegisterRequest,
)
from fsbsrc.services.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
async def register(
    data: RegisterRequest,
    db: AsyncSession = Depends(get_db),
):
    service = AuthService(db)

    return await service.register(data)


@router.post("/login")
async def login(
    data: LoginRequest,
    db: AsyncSession = Depends(get_db),
):
    service = AuthService(db)

    return await service.login(data)