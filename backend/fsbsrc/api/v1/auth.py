# Auth API routes.
# Defines HTTP endpoints for:
# - user registration
# - login
# - token generation
# 13.05.2026 (c) ilya_bisec

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from fsbsrc.core.database import get_db
from fsbsrc.schemas.user import UserCreate
from fsbsrc.services.auth_service import AuthService
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    user = await AuthService.register(
        db,
        str(user_data.email),
        user_data.username,
        user_data.password,
    )

    return {
        "message": "User created",
        "user_id": user.id,
    }


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    user = await AuthService.authenticate(
        db,
        form_data.username,
        form_data.password,
    )

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = AuthService.create_token(user)

    return {
        "access_token": token,
        "token_type": "bearer",
    }