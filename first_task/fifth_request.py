import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

new_user = {
    "address": {
        "city": "Gotham City",
        "geolocation": {
            "lat": "56.318027",
            "long": "43.944416"
        },
        "number": 1,
        "street": "Hero Filchenkov",
        "zipcode": "15253-4630"
    },
    "email": "Wayne@gmail.com",
    "name": {
        "firstname": "Bruce",
        "lastname": "Wayne"
    },
    "password": "batcave*#%*",
    "phone": "1-617-666-9669",
    "username": "batman"
}

response = requests.post(f"{BASE_URL}/users", json=new_user)

if response.status_code == 200:
    answer = response.json()

    with open('results/new_users.json', 'w') as outfile:
        json.dump(answer, outfile, indent=4)
        outfile.close()

else:
    print(f"Ошибка при выполнении запроса: {response.status_code}")
