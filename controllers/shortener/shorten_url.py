import base64
import hashlib

from sqlalchemy import func

from core.database import SessionDep
from models.urls_model import URLS
from schemas.out.shorten_url import ShortenURLOut
from services.redirect import get_complete_short_url


class ShortenUrlController:

    def shorten(self, original_url: str, session: SessionDep) -> ShortenURLOut:
        if existing_record := self.check_url_already_exists(original_url=original_url, session=session):
            return ShortenURLOut(short_url=get_complete_short_url(short_url=existing_record.short_url))
        while 1:
            # in order not to face with collision, we check if hashed_value not existed previously
            short_url = self.generate_hash_from_original_url(original_url=original_url)
            if not session.query(func.count()).filter(
                    URLS.short_url == short_url,
            ).scalar():
                new_obj = URLS(short_url=short_url, original_url=original_url)
                session.add(new_obj)
                session.commit()
                session.refresh(new_obj)
                break

        return ShortenURLOut(short_url=get_complete_short_url(short_url=short_url))

    @staticmethod
    def check_url_already_exists(original_url: str, session: SessionDep) -> URLS | None:
        return session.query(URLS).filter(URLS.original_url == original_url).first()

    @staticmethod
    def generate_hash_from_original_url(original_url: str) -> str:
        """Generate a hash for the original URL"""
        hashed_object = hashlib.sha256(original_url.encode('utf-8'))
        hash_base64 = base64.urlsafe_b64encode(hashed_object.digest()).decode('utf-8')
        return hash_base64[:5]
