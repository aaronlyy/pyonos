import requests
from pprint import pprint

prefix = "565b819e6b334859bee41adf8680cd71"
secret = "wXOf87jMiKx_4q71mWW9A-1_gUT0hlgU8yf1Ya45MS_YmLm-7xpKqI3WoSYCXF9HMgi426j2Uw0WVjyqcW8jNQ"
class Ionos:
    def __init__(self, prefix: str, secret: str) -> None:
        self._base = "https://api.hosting.ionos.com/dns/v1"
        self._headers = {"X-API-KEY": f"{prefix}.{secret}"}

    def _get(self, endpoint: str) -> dict:
        response = requests.get(f"{self._base}/{endpoint}", headers=self._headers)
        return response.json()

    def get_zones(self) -> dict:
        return self._get("/zones")

    def get_zone(self, _id: str) -> dict:
        return self._get(f"/zones/{_id}")

ionos = Ionos(prefix, secret)
pprint(ionos.get_zones())