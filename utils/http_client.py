import logging
import re
import time

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger("smoke_test")


class HttpClient:
    def __init__(self, base_url: str, login_url: str, login_return_url: str,
                 verify_ssl: bool = False, timeout: int = 30, retries: int = 2):
        self.base_url = base_url.rstrip("/")
        self.login_url = login_url
        self.login_return_url = login_return_url
        self.verify_ssl = verify_ssl
        self.timeout = timeout
        self.retries = retries
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        self._username = None
        self._password = None
        self._logged_in = False

    def login(self, username: str, password: str) -> bool:
        self._username = username
        self._password = password
        login_url = f"{self.login_url}?returnUrl={self.login_return_url}"

        # Step 1: GET login page to get CSRF token
        resp = self.session.get(login_url, verify=self.verify_ssl, timeout=self.timeout)
        if resp.status_code != 200:
            logger.error("GET login page failed: %s", resp.status_code)
            return False

        token_match = re.search(r'__RequestVerificationToken[^>]*value="([^"]+)"', resp.text)
        if not token_match:
            token_match = re.search(r'name="__RequestVerificationToken"[^>]*value="([^"]+)"', resp.text)
        csrf_token = token_match.group(1) if token_match else ""

        # Step 2: POST login
        data = {
            "ReturnUrl": self.login_return_url,
            "Client": "",
            "Ticket": "",
            "Randstr": "",
            "username": username,
            "plainPassword": password,
            "Password": password,
            "__RequestVerificationToken": csrf_token,
        }
        headers = {
            "Referer": login_url,
            "Origin": self.login_url.rsplit("/", 1)[0],
        }
        resp = self.session.post(
            login_url, data=data, headers=headers,
            allow_redirects=False, verify=self.verify_ssl, timeout=self.timeout,
        )

        if resp.status_code == 302:
            self._logged_in = True
            logger.info("Login success, cookies: %s", list(self.session.cookies.keys()))
            return True
        else:
            logger.error("Login failed: status=%s", resp.status_code)
            return False

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{path}" if path.startswith("/") else path
        kwargs.setdefault("verify", self.verify_ssl)
        kwargs.setdefault("timeout", self.timeout)

        for attempt in range(self.retries + 1):
            try:
                start = time.time()
                resp = self.session.request(method, url, **kwargs)
                elapsed = time.time() - start
                logger.info("%s %s -> %s (%.2fs)", method, url, resp.status_code, elapsed)

                # Auto re-login on 401
                if resp.status_code == 401 and self._username and attempt == 0:
                    logger.info("Got 401, re-login...")
                    self.login(self._username, self._password)
                    continue

                return resp
            except requests.RequestException as e:
                logger.warning("Request failed (attempt %d/%d): %s", attempt + 1, self.retries + 1, e)
                if attempt == self.retries:
                    raise

    def get(self, path: str, **kwargs) -> requests.Response:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs) -> requests.Response:
        return self.request("POST", path, **kwargs)
