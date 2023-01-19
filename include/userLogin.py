import asyncio
from nio import AsyncClient
from flask import session
from flask_session import Session



def clientLogin():

    client = AsyncClient(session['homeserver'])

    client.access_token = session["access_token"]
    client.user_id = session["user_id"]
    client.device_id = session["device_id"]

    asyncio.run(main(client))

async def main(client):
    response = True

    if session.get('logout_status'):
        response = await client.logout()
        print(response)

    return response