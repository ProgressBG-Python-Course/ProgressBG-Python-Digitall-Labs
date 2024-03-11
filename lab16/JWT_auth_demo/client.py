import requests

BASE_URL = 'http://127.0.0.1:8000'

def login(url):
    data = {
        'username': 'pesho',
        'password': '1234'
    }

    try:
        r = requests.post(url, data=data)
        r.raise_for_status()
        if r.ok:
            data = r.json()
            print(f'access_token: {data['access_token']}')
            return data['access_token']
        else:
            return False
    except requests.exceptions.RequestException as err:
        print(f'Request Error: {err}')



if __name__ == "__main__":
    jwt = login(f'{BASE_URL}/token')

    if jwt:
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


