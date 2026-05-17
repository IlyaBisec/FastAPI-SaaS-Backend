# Projects API routes.
# Handles project-related HTTP endpoints:
# - create projects
# - list projects
# - delete projects
# 13.05.2026 (c) ilya_bisec

from fastapi import APIRouter

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.get("")
async def get_projects():
    return {
        "message": "Projects endpoint",
    }