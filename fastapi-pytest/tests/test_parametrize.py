@pytest.mark.parametrize("item_id, expected", [
    (1, {"item_id": 1, "q": None}),
    (2, {"item_id": 2, "q": "testquery"})
])

@pytest.mark.asyncio
async def test_read_item_parametrize(client, item_id, expected):
    response = await client.get(f"/items/{item_id}")
    assert response.json() == expected
