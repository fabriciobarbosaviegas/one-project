import requests
from flask import session
from include import utils



def roomInfo(roomId):
    roomType = getRoomType(roomId)
    return {'room_id':roomId, 'room_name':getRoomName(roomId, roomType), 'room_avatar':'static/img/default.png' if getRoomAvatar(roomId, roomType) == None else getRoomAvatar(roomId, roomType)}



def getRoomType(roomId):
    room_type = requests.get(f"{session['homeserver']}/_matrix/client/r0/rooms/{roomId}/state/m.room.join_rules?access_token={session['access_token']}")
    if room_type.status_code == 200:
        room_type = room_type.json()
        return room_type['join_rule']
    else:
        return "error"



def getRoomName(roomId, roomType):

    room_name = requests.get(f"{session['homeserver']}/_matrix/client/r0/rooms/{roomId}/state/m.room.name?access_token={session['access_token']}")
    
    if roomType == 'error':
        return roomId
    
    if room_name.status_code != 200:
        avatar = utils.getAvatar(session['user_id'])
        room_name = requests.get(f"{session['homeserver']}/_matrix/client/r0/rooms/{roomId}/members?access_token={session['access_token']}")
        if room_name.status_code == 200:

            for member in room_name.json()['chunk']:
            
                if utils.convertMXC(member['content']['avatar_url']) != avatar:
            
                    return member['content']['displayname']
    
        else:
            print(room_name.json())
            return roomId

    else:
        return room_name.json()['name']



def getRoomAvatar(roomId, roomType):
    room_avatar = requests.get(f"{session['homeserver']}/_matrix/client/r0/rooms/{roomId}/state/m.room.avatar?access_token={session['access_token']}")
    print(room_avatar)
    if roomType == 'error':
        return 'static/img/default.png'

    if room_avatar.status_code != 200:

        avatar = utils.getAvatar(session['user_id'])
        room_avatar = requests.get(f"{session['homeserver']}/_matrix/client/r0/rooms/{roomId}/members?access_token={session['access_token']}")
        print(room_avatar)
        if room_avatar.status_code == 200:

            for member in room_avatar.json()['chunk']:
            
                if utils.convertMXC(member['content']['avatar_url']) != avatar:
            
                    return utils.convertMXC(member['content']['avatar_url'])

        else:
            return 'static/img/default.png'

    else:
        room_avatar = requests.get(f"{session['homeserver']}/_matrix/client/r0/rooms/{roomId}/state/m.room.avatar?access_token={session['access_token']}")
        if room_avatar.status_code == 200:

            room_avatar = room_avatar.json()

            return utils.convertMXC(room_avatar['url'])
        else:
            return 'static/img/default.png'
