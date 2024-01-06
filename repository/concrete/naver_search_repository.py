import requests
from config.naver import NAVER_CLIENT_ID, NAVER_CLIENT_SECRET


class NaverSearchRepository:
    client_id = NAVER_CLIENT_ID
    client_secret = NAVER_CLIENT_SECRET

    def __init__(self):
        pass

    def search(self, query: str, section='blog', display=100):
        response = requests.get(
            f"https://openapi.naver.com/v1/search/{section}",
            params={'query': query, 'display': display},
            headers={
                "X-Naver-Client-Id": self.client_id,
                "X-Naver-Client-Secret": self.client_secret
            }
        )

        code = response.status_code
        if code >= 400:
            raise RuntimeError(response.json())

        return response.json()
