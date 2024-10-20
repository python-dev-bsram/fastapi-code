from httpx import AsyncClient
from app.main import app
import pytest

# Basic Test Case for FastAPI root endpoint
@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# Test path and query parameters
@pytest.mark.asyncio
async def test_read_item():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/items/42?q=testquery")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "testquery"}

# Test authentication logic
@pytest.mark.asyncio
async def test_protected_route():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        headers = {"Authorization": "Bearer valid-token"}
        response = await ac.get("/protected", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": "Authenticated!"}

@pytest.mark.asyncio
async def test_protected_route_unauthenticated():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        headers = {"Authorization": "Bearer invalid-token"}
        response = await ac.get("/protected", headers=headers)
    assert response.status_code == 401
