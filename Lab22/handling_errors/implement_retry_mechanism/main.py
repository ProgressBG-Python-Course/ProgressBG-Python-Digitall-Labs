import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def requests_retry_session(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504), session=None):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

try:
    session = requests_retry_session()
    response = session.get('https://example.com')
    response.raise_for_status()
    print(response.text)
except requests.exceptions.HTTPError as e:
    print(f"HTTPError: {e}")
except requests.exceptions.ConnectionError as e:
    print(f"ConnectionError: {e}")
except requests.exceptions.Timeout as e:
    print(f"Timeout: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")