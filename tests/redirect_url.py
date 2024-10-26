from unittest.mock import patch

from fastapi.testclient import TestClient
from starlette import status

from core.fastapi import app

client = TestClient(app)


def test_redirect_valid_short_url():
    with patch("controllers.redirect.redirect_url.RedirectURLController.get_redirect_url") as mock_get_redirect_url:
        mock_get_redirect_url.return_value = ["https://www.test.com"]
        response = client.get("/test123")
        assert response.status_code == status.HTTP_302_FOUND
        assert response.headers["Location"] == "https://www.test.com"
