from fastapi import APIRouter, Path
from starlette import status
from starlette.exceptions import HTTPException
from starlette.responses import RedirectResponse
from starlette.status import HTTP_404_NOT_FOUND

from controllers.redirect.redirect_url import RedirectURLController
from core.database import SessionDep
from proxies.redis import redis_proxy

router = APIRouter(
    prefix="",
    tags=[
        "redirect",
    ]
)


@router.get(path="/{short_url}", response_class=RedirectResponse, status_code=status.HTTP_302_FOUND)
async def redirect(
        session: SessionDep,
        short_url: str = Path(..., description="Shorten URL"),
):
    original_url = RedirectURLController().get_redirect_url(short_url=short_url, session=session)
    if not original_url:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND)

    try:
        redis_proxy.set(name=short_url, value=original_url[0], ex=60 * 60 * 24)
    except Exception:
        pass
    return original_url[0]
