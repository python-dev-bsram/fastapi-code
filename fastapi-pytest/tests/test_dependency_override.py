from app.main import app, fake_authentication
from fastapi import HTTPException, status
import pytest


# pass token when invalid and test using mock
async def mock_authentication(token: str):
    if token == "invalid-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
    return True


@pytest.mark.asyncio
async def test_protected_route_with_mock(client):
    app.dependency_overrides[fake_authentication] = mock_authentication
    response = await client.get("/protected?token=valid-token")
    assert response.status_code == 200
    assert response.json() == {"message": "Authenticated!"}


@pytest.mark.asyncio
async def test_protected_route_with_invalid_token(client):
    app.dependency_overrides[fake_authentication] = mock_authentication
    response = await client.get("/protected?token=invalid-token")
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid token"}
