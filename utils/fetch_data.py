import requests
from requests import Response

def hit_url(url) -> Response:
    result_=requests.get(url)
    if result_.status_code!=200:
        result_.raise_for_status()
    else:
        return result_