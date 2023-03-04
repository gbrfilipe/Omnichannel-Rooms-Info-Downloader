from datetime import datetime
import requests as req
from tqdm import tqdm
import pandas as pd
import math

x_auth_token = "ABC"
x_user_id = "DEF"
url = "https://abc.def" # Without the end slash, example: https://chat.domain.com
filename = f'export-{datetime.now().strftime("%d-%m-%Y-%H-%M-%S")}.csv'

def rooms_list(x_auth_token: str, x_user_id: str, offset: int, url: str):
    url_rooms = url + f"/api/v1/livechat/rooms?offset={offset}"

    headers = {
        'X-Auth-Token': x_auth_token,
        'X-User-Id': x_user_id
    }

    response_rooms = req.get(url_rooms, headers=headers).json()
    
    return response_rooms

offset = 0
lista_salas = []

retorno = rooms_list(x_auth_token, x_user_id, offset, url)
total = retorno.get("total")
count = retorno.get("count")
total_iterations = total / count

for i in tqdm(range(math.ceil(total_iterations))):
        retorno = rooms_list(x_auth_token, x_user_id, offset, url)
        total_rooms = retorno.get("total")
        lista_salas.extend(retorno.get("rooms"))
        offset += count

df = pd.json_normalize(lista_salas)
df.to_csv(filename, index=False)