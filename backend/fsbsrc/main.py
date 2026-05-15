# Application entry point.
# Initializes FastAPI app and includes all API routers.
# This is the file that starts the backend server.
# 13.05.2026 (c) ilya_bisec

from fastapi import FastAPI

from fsbsrc.api.v1.auth import router as auth_router


app = FastAPI(
    title="FastAPI SaaS Backend",
)


app.include_router(auth_router)


@app.get("/")
async def root():
    return {
        "message": "Backend running",
    }