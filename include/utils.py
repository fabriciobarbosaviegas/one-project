import requests
from flask import session
from datetime import datetime, timedelta


def getAvatar(userName):
    iam = requests.get(f'{session["homeserver"]}/_matrix/client/v3/profile/{userName}')
    if 'avatar_url' in iam.json():
        avatarData = iam.json()['avatar_url']

        return convertMXC(avatarData)
    
    else:
        return False



def convertMXC(mxcUrl):
    mxcData = mxcUrl.split('/')[-2:]
    
    return f"https://matrix.onemessenger.tk/_matrix/media/r0/thumbnail/{mxcData[0]}/{mxcData[1]}?width=32&height=32"



def getJoinedRooms():
        joins = requests.get(f'{session["homeserver"]}/_matrix/client/v3/joined_rooms?access_token={session["access_token"]}')
        if joins.status_code == 200:
            return joins.json()['joined_rooms']
        else:
            return []



def convertTime(timestamp):
    time = datetime.fromtimestamp(timestamp / 1000)
    date = time.strftime("%Y/%m/%d")
    today = datetime.today()
    lastWeek = datetime.today() - timedelta(days = 7)

    if date == today.strftime("%Y/%m/%d"):
        return time.strftime("%H:%M")
    elif time >= lastWeek:
        return time.strftime("%A")[0:3]
    else:
        return date



def hello(name):
    return f'Hello, {name}'