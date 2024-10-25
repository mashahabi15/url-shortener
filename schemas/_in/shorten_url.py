from pydantic import BaseModel


class ShortenURLIn(BaseModel):
    original_url: str
