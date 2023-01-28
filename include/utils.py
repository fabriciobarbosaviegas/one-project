import requests
from flask import session
from flask_session import Session



def getAvatar(userName):
    print(session["homeserver"])
    iam = requests.get(f'{session["homeserver"]}/_matrix/client/v3/profile/{userName}')
    if 'avatar_url' in iam.json():
        avatarData = iam.json()['avatar_url'].split('/')[-2:]

        return f"https://matrix.onemessenger.tk/_matrix/media/r0/thumbnail/{avatarData[0]}/{avatarData[1]}?width=32&height=32"
    
    else:
        return False



def getJoinedRooms():
        joins = requests.get(f'{session["homeserver"]}/_matrix/client/v3/joined_rooms?access_token={session["access_token"]}')

        return joins
