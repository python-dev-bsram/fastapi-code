from app.main import app, fake_authentication

def mock_authentication(token: str):
    return ""

@pytest.mark.asyncio
async def test_protected_route_with_mock(client):
    app.dependency_overrides[fake_authentication] = mock_authentication
    response = await client.get("/protected")
    assert response.status_code == 200
    assert response.json() == {"message": "Authenticated!"}
