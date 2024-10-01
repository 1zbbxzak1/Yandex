import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

response = requests.get(f"{BASE_URL}/users")

if response.status_code == 200:
    users = response.json()

    with open('results/users.json', 'w') as outfile:
        json.dump(users, outfile, indent=4)
        outfile.close()

else:
    print(f"Ошибка при выполнении запроса: {response.status_code}")
