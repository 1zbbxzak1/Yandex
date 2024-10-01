import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

response = requests.get(f"{BASE_URL}/products")

if response.status_code == 200:
    products = response.json()

    # Фильтруем продукты по цене < 20
    filtered_products = [product for product in products if product.get('price', 0) < 20]

    # Сохраняем отфильтрованные данные в файл
    with open('results/filtered_products.json', 'w') as outfile:
        json.dump(filtered_products, outfile, indent=4)
        outfile.close()
else:
    print(f"Ошибка при выполнении запроса: {response.status_code}")
