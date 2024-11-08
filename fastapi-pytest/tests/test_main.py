from httpx import AsyncClient
from app.main import app
import pytest

# Basic Test Case for FastAPI root endpoint
@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# Test path and query parameters
@pytest.mark.asyncio
async def test_read_item():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/items/42?q=testquery")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "testquery"}

