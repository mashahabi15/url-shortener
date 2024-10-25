from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    port: int = 8000
    ENVIRONMENT: str = "DEVELOPMENT"
    WORKERS: int = 1
    BASE_URL: str = "http://localhost:8000"

    SENTRY_DSN: str = "https://SENTRY_DSN_URL:PORT"

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore
