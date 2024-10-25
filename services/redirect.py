from core.config import settings


def get_complete_short_url(short_url: str) -> str:
    return f"{settings.BASE_URL}/{short_url}"
