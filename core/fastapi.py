from fastapi import FastAPI

from routers import default_router
from .config import settings

origins: list = ["*"]


def init_routers(app_: FastAPI) -> FastAPI:
    app_.include_router(default_router)
    return app_


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="URL Shortener Backend",
        description="URL Shortener Backend",
        version="0.1.0",
        docs_url=None if settings.ENVIRONMENT == "production" else "/docs",
        redoc_url=None if settings.ENVIRONMENT == "production" else "/redoc",
    )
    app_ = init_routers(app_=app_)
    return app_


# NOTE commenting due to not having sentry service at the moment
# sentry_sdk.init(
#     dsn=settings.SENTRY_DSN,
# integrations=[FastApiIntegration()],
# Set traces_sample_rate to 1.0 to capture 100%
# of transactions for performance monitoring.
# We recommend adjusting this value in production.
# traces_sample_rate=1.0,
# )

app = create_app()
