import requests


BASE_URL = 'http://127.0.0.1:8000'

jwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwZXNobyIsImV4cCI6MTcxMDE3MjA1NX0.wZc6VswKNFlIzEGtAzRwQMhoPy4I7Gbcm4SAgB2uhR8'

headers = {
    'Authorization': f'Bearer {jwt}'
}

try:
    r = requests.get(f'{BASE_URL}/users/me', headers=headers)
    r.raise_for_status()
    if r.ok:
        data = r.json()
        print(data)
except requests.exceptions.RequestException as err:
    print(f'Request Error: {err}')