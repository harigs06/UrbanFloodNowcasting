"""API Authentication and Redis-backed Rate Limiting."""

import time
from typing import Dict, Optional
from fastapi import Header, HTTPException, Request, Security, status
from fastapi.security.api_key import APIKeyHeader

from src.config import settings

API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)

# In-memory rate-limiter fallback when Redis is absent: ip/key -> list of timestamps
_rate_limit_memory_store: Dict[str, list] = {}


async def verify_api_key(
    api_key: Optional[str] = Security(API_KEY_HEADER),
) -> str:
    """Validates the provided X-API-Key header against configured API keys."""
    # In development / testing, allow pass-through if configured
    if settings.DEBUG and not api_key:
        return "dev-user"

    if not api_key or api_key not in settings.API_KEYS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing X-API-Key header.",
        )
    return api_key


async def check_rate_limit(
    request: Request,
    api_key: Optional[str] = Security(API_KEY_HEADER),
) -> None:
    """Enforces sliding-window rate limiting per client IP or API key."""
    client_id = api_key or request.client.host if request.client else "unknown_client"
    now = time.time()
    window_sec = 60.0
    limit = settings.RATE_LIMIT_PER_MINUTE

    # In-memory sliding window
    timestamps = _rate_limit_memory_store.get(client_id, [])
    # Prune timestamps older than 60 seconds
    timestamps = [t for t in timestamps if now - t < window_sec]

    if len(timestamps) >= limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Rate limit exceeded: maximum {limit} requests per minute.",
        )

    timestamps.append(now)
    _rate_limit_memory_store[client_id] = timestamps
