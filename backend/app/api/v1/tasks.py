# Tasks -
# 13.05.2026 (c) ilya_bisec

from fastapi import APIRouter
from fastapi import Query


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("")
async def get_tasks(
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=100),
    status: str | None = None,
):
    return {
        "page": page,
        "limit": limit,
        "status": status,
    }