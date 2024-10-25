from pydantic import BaseModel


class ShortenURLOut(BaseModel):
    short_url: str
