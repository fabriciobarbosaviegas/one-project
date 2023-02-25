import requests
from flask import session
from include import utils as ut
import json



def send_message(room_id, message):
    url = f"https://matrix.org/_matrix/client/r0/rooms/{room_id}/send/m.room.message"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {session['access_token']}"
    }

    data = {
        "msgtype": "m.text",
        "body": message
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))

    print(response.json)

    if response.status_code == 200:
        print("Mensagem enviada com sucesso!")
    else:
        print(f"Erro ao enviar mensagem: {response.text}")