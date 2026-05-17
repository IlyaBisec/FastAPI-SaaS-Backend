# Tasks API routes.
# Handles task-related HTTP endpoints:
# - list tasks
# - filtering
# - pagination
# 13.05.2026 (c) ilya_bisec

from typing import Optional

from fastapi import APIRouter, Query

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("")
async def get_tasks(
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=100),
    status: Optional[str] = None,
):
    return {
        "page": page,
        "limit": limit,
        "status": status,
    }