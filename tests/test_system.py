from app import __version__
from tests.conftest import client


class TestPing:
    def it_returns_the_correct_value(_):
        response = client.get(url="/ping")
        assert response.status_code == 200
        assert response.json() == [True]
