import requests as req
import pandas as pd
from datetime import datetime

x_auth_token = "XXXYYYZZZ"
x_user_id = "ZZZYYYXXX"
url = "https://xyz.com" # Without the end slash, example: https://chat.domain.com

filename = f'export-{datetime.now().strftime("%d-%m-%Y-%H-%M-%S")}.csv'

def rooms_list(x_auth_token: str, x_user_id: str, url: str):
    url_rooms = url + "/api/v1/livechat/rooms"

    headers = {
        'X-Auth-Token': x_auth_token,
        'X-User-Id': x_user_id
    }

    response_rooms = req.get(url_rooms, headers=headers).json()

    return response_rooms

df = pd.json_normalize(rooms_list(x_auth_token, x_user_id, url)["rooms"])

df.to_csv(filename)
