import uvicorn

from core.config import settings

if __name__ == "__main__":
    uvicorn.run(
        host="0.0.0.0",
        port=settings.port,
        app="core.fastapi:app",
        reload=True if settings.ENVIRONMENT != "production" else False,
        workers=settings.WORKERS,
    )
