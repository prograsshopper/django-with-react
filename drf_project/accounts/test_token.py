import requests
import os

JWT_TOKEN = os.environ["JWT_TOKEN"]

headers = {
    'Authorization': f'JWT {JWT_TOKEN}'
}

res = requests.get("http://127.0.0.1:60592/post/", headers=headers)
print(res.json())