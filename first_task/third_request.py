import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

response = requests.get(f"{BASE_URL}/products/category/jewelery")

if response.status_code == 200:
    jewelery = response.json()

    with open('results/jewelery.json', 'w') as outfile:
        json.dump(jewelery, outfile, indent=4)
        outfile.close()

else:
    print(f"Ошибка при выполнении запроса: {response.status_code}")
