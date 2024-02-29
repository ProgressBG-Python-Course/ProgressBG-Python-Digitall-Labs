import re
import requests
from typing import List,Optional

def download_image(url:str)->Optional[bytes]:
    # print(f'Downloading {url}')
    response = requests.get(url)
    if response and response.ok:
        return response.content
    else:
        print(f'Can not download {url}')

def write_to_file(filename:str, bytes:bytes):
    with open(filename, 'wb') as fh:
        fh.write(bytes)


def make_filename(url:str)->str:
    rx = re.compile(r'\/([\w-]+)\.(\w{3,4})$')
    match = rx.search(url)
    if match:
        return match.group(1) + '.' + match.group(2)
    else:
        return url
