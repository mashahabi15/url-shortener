from core.database import SessionDep
from models.urls_model import URLS


class RedirectURLController:
    def get_redirect_url(self, short_url: str, session: SessionDep):
        return session.query(URLS.original_url).filter(URLS.short_url == short_url).first()
