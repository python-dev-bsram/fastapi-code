from app.db import SessionLocal
from app.main import app
import pytest

@pytest.fixture
def override_get_db():
    def _override_get_db():
        db = SessionLocal()
        yield db
    app.dependency_overrides[get_db] = _override_get_db

@pytest.mark.asyncio
async def test_create_item(client, override_get_db):
    response = await client.post("/items", json={"name": "Item"})
    assert response.status_code == 201
