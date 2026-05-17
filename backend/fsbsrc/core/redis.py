# 16.05.2026 (c) ilya_bisec

from redis.asyncio import Redis

from fsbsrc.core.config import settings

redis = Redis.from_url(settings.REDIS_URL)