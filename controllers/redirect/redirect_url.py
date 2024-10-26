from core.database import SessionDep
from models.urls_model import URLS
from proxies.redis import redis_proxy


class RedirectURLController:
    def get_redirect_url(self, short_url: str, session: SessionDep):
        try:
            if original_url := redis_proxy.get(short_url):
                return original_url
        except Exception:
            pass
        return session.query(URLS.original_url).filter(URLS.short_url == short_url).first()
