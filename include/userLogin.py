import asyncio
from nio import AsyncClient
from flask import session
from flask_session import Session

def clientLogin(username='', password='', homeserver='', checkLogout = False):
    if not session.get('access_token') and checkLogout == False:   
        print('login')
        client = AsyncClient(
            homeserver, 
            username
        )
        
        response = asyncio.run(login(client, password))

        return response
    
    elif session.get('access_token') and checkLogout == False:
        print(session['homeserver'])
        client = AsyncClient(session['homeserver'])

        client.access_token = session["access_token"]
        client.user_id = session["user_id"]
        client.device_id = session["device_id"]

        return response

    elif checkLogout:
        print('logout')
        response = clientLogout(client)
    
        return response



async def login(client, password):
    response = await client.login(password)

    return response



async def clientLogout(client):
    response = await client.logout()
    
    return response