import pytest


@pytest.mark.parametrize(
    "item_id, query, expected",
    [
        (1, None, {"item_id": 1, "q": None}),
        (2, "testquery", {"item_id": 2, "q": "testquery"}),
    ],
)
@pytest.mark.asyncio
async def test_read_item_parametrize(client, item_id, query, expected):
    # Conditionally include the query parameter in the URL
    url = f"/items/{item_id}"
    if query:
        url += f"?q={query}"

    response = await client.get(url)
    assert response.json() == expected
