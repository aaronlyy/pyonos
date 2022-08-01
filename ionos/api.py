import requests

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