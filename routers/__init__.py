from fastapi import APIRouter
from .shorten_url import router as shorten_url_router

routers = APIRouter(prefix="/api/v1")

routers.include_router(router=shorten_url_router)
