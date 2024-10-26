from starlette import status
from starlette.testclient import TestClient

from core.fastapi import app

client = TestClient(app)


def test_shorten_url():
    response = client.post(url="/api/v1/shorten_url", json={"original_url": "https://google.com"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("short_url") is not None
