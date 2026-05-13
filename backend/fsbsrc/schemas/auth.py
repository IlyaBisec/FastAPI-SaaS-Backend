# Authentication schemas.
# Defines request/response models for login and registration.
# 13.05.2026 (c) ilya_bisec

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str