import logging
import os
import requests

BASE_URL = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
TIMEOUT = 10
log = logging.getLogger("api")


class BaseClient:
    def api_request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = f"{BASE_URL}{path}"
        log.info("%s %s", method, url)
        response = requests.request(method, url, timeout=TIMEOUT, **kwargs)
        log.info("-> %s", response.status_code)
        return response
