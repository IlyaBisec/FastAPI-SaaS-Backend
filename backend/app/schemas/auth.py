# Auth -
# 13.05.2026 (c) ilya_bisec

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str