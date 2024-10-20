
# What You Will Learn

By the end of this guide, you will understand how to:

1. **Set up Pytest for FastAPI**:
   - Install the necessary libraries (`pytest`, `pytest-asyncio`, `httpx`) and configure testing for FastAPI apps.

2. **Test Basic FastAPI Applications**:
   - Create and run basic test cases to verify FastAPI endpoints using asynchronous requests.

3. **Test Path and Query Parameters**:
   - Learn how to test endpoints that accept path and query parameters.

4. **Use Fixtures for Setup and Teardown**:
   - Implement reusable fixtures for setting up resources (e.g., test clients) before and after tests.

5. **Mock External Dependencies**:
   - Utilize FastAPI’s `dependency_overrides` to mock dependencies like databases or external services during testing.

6. **Test Authentication**:
   - Learn to test endpoints that require authentication (OAuth2, JWT, etc.) using custom headers.

7. **Test Database Operations**:
   - Set up mock databases or in-memory databases (SQLite) to test database operations effectively during development.

8. **Apply Advanced Pytest Techniques**:
   - Parameterize tests to run with multiple data sets.
   - Handle asynchronous functions in fixtures.
   - Test WebSocket connections in FastAPI apps.

9. **Generate Test Coverage Reports**:
   - Use `pytest-cov` to generate coverage reports, ensuring thorough test coverage for your FastAPI application.

This guide prepares you with the necessary tools and techniques to effectively test your FastAPI applications, covering both basic and advanced testing scenarios.



#### Setup of Pytest for FastAPI

Ensure you have the required libraries installed:

```bash
pip install pytest pytest-asyncio httpx
```



`httpx` is used for async HTTP requests, and `pytest-asyncio` is necessary for testing asynchronous endpoints.

## Single View to Understand the Pytest
---

#### Basic FastAPI App Example

Here is a simple FastAPI app that we'll use for testing:

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

#### Basic Pytest Test Case

The first step is to use FastAPI's TestClient from `httpx` to test your API.

```python
# test_main.py
from httpx import AsyncClient
from main import app
import pytest

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
```

This test simulates a GET request to the root endpoint and checks that it returns the correct status code and JSON response.

#### Testing with Path and Query Parameters

For endpoints that accept parameters:

```python
@pytest.mark.asyncio
async def test_read_item():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/items/42?q=testquery")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "testquery"}
```

#### Using Fixtures for Setup and Teardown

Fixtures can be used to set up resources before tests and tear them down afterward. This can include setting up a database connection, initializing state, etc.

```python
# conftest.py
import pytest
from httpx import AsyncClient
from main import app

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
```

You can then inject the `client` fixture into your tests:

```python
@pytest.mark.asyncio
async def test_read_root(client):
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
```

#### Mocking Dependencies

FastAPI allows dependency injection, and you can mock dependencies in your tests using `dependency_overrides`.

Example: Mocking a dependency that provides a database connection or an external service.

```python
# main.py
from fastapi import Depends

def common_dependency():
    return "real dependency"

@app.get("/dependency")
async def dependency_route(dep: str = Depends(common_dependency)):
    return {"dependency": dep}
```

In your test:

```python
def mock_dependency():
    return "mocked dependency"

@pytest.mark.asyncio
async def test_dependency_route(client):
    app.dependency_overrides[common_dependency] = mock_dependency
    response = await client.get("/dependency")
    assert response.json() == {"dependency": "mocked dependency"}
```

#### Testing Authentication

FastAPI provides support for authentication mechanisms like OAuth2, JWT, etc. Here’s an example of how to test routes that require authentication:

```python
# main.py
from fastapi import Depends, HTTPException, status

def fake_authentication(token: str):
    if token != "valid-token":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

@app.get("/protected")
async def protected_route(token: str = Depends(fake_authentication)):
    return {"message": "Authenticated!"}
```

Test this using a header injection:

```python
@pytest.mark.asyncio
async def test_protected_route(client):
    headers = {"Authorization": "Bearer valid-token"}
    response = await client.get("/protected", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": "Authenticated!"}

@pytest.mark.asyncio
async def test_protected_route_unauthenticated(client):
    headers = {"Authorization": "Bearer invalid-token"}
    response = await client.get("/protected", headers=headers)
    assert response.status_code == 401
```

#### Database Testing with Pytest

You can mock database operations or use a test database. One common technique is to use SQLite in memory for fast tests or set up a temporary PostgreSQL/MySQL database.

Here’s an example of using an in-memory SQLite database:

```python
# db.py
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

Then, override the database dependency in the test:

```python
from db import get_db

@pytest.fixture
def override_get_db():
    def _override_get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    app.dependency_overrides[get_db] = _override_get_db

@pytest.mark.asyncio
async def test_create_item(client, override_get_db):
    response = await client.post("/items", json={"name": "Item"})
    assert response.status_code == 201
```

#### Advanced Pytest Techniques

##### Parameterization

To run the same test function with different data:

```python
@pytest.mark.parametrize("item_id, expected", [
    (1, {"item_id": 1, "q": None}),
    (2, {"item_id": 2, "q": "test"}),
])
@pytest.mark.asyncio
async def test_read_item(client, item_id, expected):
    response = await client.get(f"/items/{item_id}")
    assert response.json() == expected
```

##### Handling Async Functions in Fixtures

You can use `pytest-asyncio` to handle async fixtures:

```python
@pytest.fixture
async def setup_db():
    await some_async_setup()
    yield
    await some_async_teardown()
```

##### Testing WebSockets

If your FastAPI app uses WebSockets, pytest can be used to test WebSocket connections as well.

```python
@pytest.mark.asyncio
async def test_websocket():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        with ac.websocket_connect("/ws") as websocket:
            websocket.send_json({"msg": "Hello"})
            data = websocket.receive_json()
            assert data == {"msg": "Hello"}
```

#### Test Coverage

You can generate coverage reports using the `pytest-cov` plugin:

```bash
pip install pytest-cov
pytest --cov=main
```

This will display a report of which parts of your code are covered by tests.

#### How to Run the tests 

1. Run all the test command

    ```bash
    pytest
    ```

2. Run tests from a specific directory
   
    ```bash
    pytest tests/
    ```
