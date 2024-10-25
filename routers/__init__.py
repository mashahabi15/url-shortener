from fastapi import APIRouter

from .redirect_url import router as redirect_url_router
from .shorten_url import router as shorten_url_router

versioning_api_router = APIRouter(prefix="/api/v1")
default_router = APIRouter(prefix="")

versioning_api_router.include_router(router=shorten_url_router)
default_router.include_router(router=versioning_api_router)
default_router.include_router(router=redirect_url_router)
