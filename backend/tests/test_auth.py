async def test_register(client):
    response = await client.post(
        "/auth/register",
        json={
            "email": "test@test.com",
            "username": "test",
            "password": "12345678",
        },
    )

    assert response.status_code == 200