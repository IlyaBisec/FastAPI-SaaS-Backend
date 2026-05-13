# Application entry point.
# Initializes FastAPI app and includes all API routers.
# This is the file that starts the backend server.
# 13.05.2026 (c) ilya_bisec

from fastapi import FastAPI

from fsbsrc.api.v1.auth import router as auth_router
from fsbsrc.api.v1.tasks import router as tasks_router

app = FastAPI(
    title="Production FastAPI Backend",
    version="1.0.0",
)


app.include_router(auth_router)
app.include_router(tasks_router)