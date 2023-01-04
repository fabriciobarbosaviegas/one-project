import asyncio
from nio import AsyncClient

def clientLogin(username, password, homeserver):
    client = AsyncClient(
        homeserver, 
        username
    )
    
    response = asyncio.run(login(client, password))

    return response


async def login(client, password):
    response = await client.login(password)

    return response