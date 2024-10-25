from fastapi import APIRouter

from controllers.shortener.shorten_url import ShortenUrlController
from schemas._in.shorten_url import ShortenURLIn
from schemas.out.shorten_url import ShortenURLOut

router = APIRouter(
    prefix="",
    tags=[
        "shorten_url",
    ],
)


@router.post("/shorten_url", response_model=ShortenURLOut)
async def register(
        data: ShortenURLIn,
) -> ShortenURLOut:
    return ShortenUrlController().shorten(original_url=data.original_url)
