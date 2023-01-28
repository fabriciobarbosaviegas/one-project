import requests
from flask import session
from include import utils



def roomInfo(roomId):
    roomType = getRoomType(roomId)
    return {'room_id':roomId, 'room_name':getRoomName(roomId, roomType), 'room_avatar':getRoomAvatar(roomId, roomType)}



def getRoomType(roomId):
    room_type = requests.get("https://matrix.onemessenger.tk/_matrix/client/r0/rooms/"+roomId+"/state/m.room.join_rules?access_token="+session['access_token'])
    if room_type.status_code == 200:
        room_type = room_type.json()
        return room_type['join_rule']
    else:
        return "error"



def getRoomName(roomId, roomType):
    if roomType == 'invite':
        avatar = utils.getAvatar(session['user_id'])
        room_name = requests.get("https://matrix.onemessenger.tk/_matrix/client/r0/rooms/"+roomId+"/members?access_token="+session['access_token'])
        if room_name.status_code == 200:

            for member in room_name.json()['chunk']:
            
                if utils.convertMXC(member['content']['avatar_url']) != avatar:
            
                    return member['content']['displayname']
    
    elif roomType == 'error':
        return roomId

    else:
        room_name = requests.get("https://matrix.onemessenger.tk/_matrix/client/r0/rooms/"+roomId+"/state/m.room.name?access_token="+session['access_token'])

        if room_name.status_code == 200:

            room_name = room_name.json()

            return room_name['name']



def getRoomAvatar(roomId, roomType):
    if roomType == 'invite':
        avatar = utils.getAvatar(session['user_id'])
        room_name = requests.get("https://matrix.onemessenger.tk/_matrix/client/r0/rooms/"+roomId+"/members?access_token="+session['access_token'])
        
        if room_name.status_code == 200:

            for member in room_name.json()['chunk']:
            
                if utils.convertMXC(member['content']['avatar_url']) != avatar:
            
                    return utils.convertMXC(member['content']['avatar_url'])
    
    elif roomType == 'error':
        return 'static/img/default.png'

    else:
        room_avatar = requests.get("https://matrix.onemessenger.tk/_matrix/client/r0/rooms/"+roomId+"/state/m.room.avatar?access_token="+session['access_token'])

        if room_avatar.status_code == 200:

            room_avatar = room_avatar.json()

            #print(room_avatar['url'])

            return utils.convertMXC(room_avatar['url'])