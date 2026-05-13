# Auth -
# 13.05.2026 (c) ilya_bisec

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.auth import Token
from app.schemas.user import UserCreate
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register(
        data: UserCreate,
        db: AsyncSession = Depends(get_db),
):
    repository = UserRepository(db)
    service = AuthService(repository)

    user = await service.register(data.email, data.password)

    return user


@router.post("/login", response_model=Token)
async def login(
        data: UserCreate,
        db: AsyncSession = Depends(get_db),
):
    repository = UserRepository(db)
    service = AuthService(repository)

    token = await service.login(data.email, data.password)

    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "access_token": token,
        "token_type": "bearer",
    }
