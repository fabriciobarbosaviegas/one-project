import requests
from flask import session
from include import utils as ut



def getMessages(room, limit=0):
    headers = {
        "Authorization": f"Bearer {session['access_token']}"
    }

    message = requests.get( f"{session['homeserver']}/_matrix/client/r0/rooms/{room}/messages?dir=b", headers=headers)

    if message.status_code == 200:
        messagesContent = {room:{"content":[], "sender":[], "time":[]}}
        messages = message.json()["chunk"]

        if isCypher(messages):
            return messagesContent

        elif isCypher(messages) == 'error':
            return messagesContent

        else:
            if limit == 0:
                for message in messages:
                    messagesContent[room]['content'].append(message['content']['body'])
                    messagesContent[room]['sender'].append(message['sender'] if message['sender'] != session['user_id'] else 'you')
                    messagesContent[room]['time'].append(ut.convertTime(message['origin_server_ts']))

            else:

                c = 0

                for message in messages:
                    c += 1

                    messagesContent[room]['content'].append(message['content']['body'])
                    messagesContent[room]['sender'].append(message['sender'] if message['sender'] != session['user_id'] else 'you')
                    messagesContent[room]['time'].append(ut.convertTime(message['origin_server_ts']))

                    if c == limit:
                        break

            return messagesContent                    


    else:
        return ''



def isCypher(messages):
    for message in messages:
        if message['type'] == 'm.room.encrypted':
            return True
        elif message['type'] == 'm.room.message':
            return False
        else:
            return 'error'