import pytest
from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.fixture
def dummy_fixture():
    raise NotImplementedError
