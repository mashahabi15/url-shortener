from sqlmodel import SQLModel, Field


class URLS(SQLModel, table=True):
    id: int = Field(primary_key=True)
    original_url: str | None
    short_url: str | None = Field(index=True, unique=True)
