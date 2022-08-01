import requests

class Dns:
    def __init__(self, prefix: str, secret: str) -> None:
        self._base = "https://api.hosting.ionos.com/dns/v1"
        self._headers = {"X-API-KEY": f"{prefix}.{secret}", "Content-Type": "application/json"}

    def _get(self, endpoint: str) -> dict:
        print(f"{self._base}{endpoint}")
        response = requests.get(f"{self._base}{endpoint}", headers=self._headers)
        return (response.status_code, response.json())
    
    def _patch(self, endpoint: str, data: dict) -> dict:
        print(f"{self._base}{endpoint}")
        response = requests.patch(f"{self._base}{endpoint}", json=data, headers=self._headers)
        return (response.status_code, None)

    def _put(self, endpoint: str, data: dict) -> dict:
        print(f"{self._base}{endpoint}")
        response = requests.put(f"{self._base}{endpoint}", json=data, headers=self._headers)
        return (response.status_code, None)

    # --- ZONES ---
    def get_zones(self) -> tuple:
        """Returns list of customer zones.

        Returns:
            tuple: (status_code, json)
        """
        return self._get("/zones")

    def get_zone(self, zone_id: str) -> tuple:
        """Returns a customer zone.

        Args:
            zone_id (str)

        Returns:
            tuple: (status_code, json)
        """
        return self._get(f"/zones/{zone_id}")

    def patch_zone(self, zone_id: int, data: list) -> tuple:
        """Replaces all records of the same name and type with the ones provided.

        Args:
            zone_id (int)
            data (list)

        Returns:
            tuple: (status_code, json)
        """
        return self._patch(f"/zones/{zone_id}", data=data)

    def put_zone(self, zone_id: int, data: list) -> tuple:
        """Replaces all records in the zone with the ones provided.

        Args:
            zone_id (int)
            data (list)

        Returns:
            tuple: (status_code, json)
        """
        return self._put(f"/zones/{zone_id}", data=data)