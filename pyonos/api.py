import requests

class PyonosResponse:
    def __init__(self, response: requests.Response) -> None:
        self._status_code = response.status_code
        content_type = response.headers.get("Content-Type")

        if "application/json" in content_type:
            self._json = response.json()
        else:
            self._json = None
    
    @property
    def status_code(self) -> int:
        return self._status_code

    @property
    def json(self):
        return self._json

    def __str__(self) -> str:
        s = f"[{self.status_code}]\n{self.json}"
        return s

class Dns:
    def __init__(self, prefix: str, secret: str) -> None:
        self._base = "https://api.hosting.ionos.com/dns/v1"
        self._headers = {"X-API-KEY": f"{prefix}.{secret}"}

    def _request(self, method: str, endpoint: str, params: dict = None, data: list = None) -> tuple:
        method = method.lower()
        url = f"{self._base}{endpoint}"
        if method == "get":
            response = requests.get(url, params=params, headers=self._headers)
        elif method == "patch":
            response = requests.patch(url, json=data, headers=self._headers)
        elif method == "put":
            response = requests.put(url, json=data, headers=self._headers)
        elif method == "post":
            response = requests.post(url, json=data, headers=self._headers)
        elif method == "delete":
            response = requests.delete(url, headers=self._headers)
        else:
            raise Exception
        return PyonosResponse(response)

    # --- ZONES ---
    def get_zones(self) -> PyonosResponse:
        """Returns list of customer zones.

        Returns:
            PyonosResponse
        """
        return self._request("GET", "/zones")

    def get_zone(self, zone_id: str, suffix: str = None, record_name: str = None, record_type: str = None) -> PyonosResponse:
        """Returns a customer zone.

        Args:
            zone_id (str)
            suffix (str, optional): The FQDN used to filter all the record names that end with it.
            record_name (str, optional): The record names that should be included (same as name field of Record).
            record_type (str, optional): A comma-separated list of record types that should be included.

        Returns:
            PyonosResponse
        """
        params = {
            "suffix": suffix,
            "recordName": record_name,
            "recordType": record_type
        }
        return self._request("GET", f"/zones/{zone_id}", params=params)

    def patch_zone(self, zone_id: int, records: list) -> PyonosResponse:
        """Replaces all records of the same name and type with the ones provided.

        Args:
            zone_id (int)
            data (list)

        Returns:
            PyonosResponse
        """
        return self._request("PATCH", f"/zones/{zone_id}", data=records)

    def put_zone(self, zone_id: int, records: list) -> PyonosResponse:
        """Replaces all records in the zone with the ones provided.

        Args:
            zone_id (int)
            data (list)

        Returns:
            PyonosResponse
        """
        return self._request("PUT", f"/zones/{zone_id}", data=records)

    # --- RECORDS ---
    def post_records(self, zone_id: str, records: list) -> PyonosResponse:
        """Creates records for a customer zone.

        Args:
            zone_id (str)
            records (list): List of record dictionaries

        Returns:
            PyonosResponse
        """
        return self._request("POST", f"/zones/{zone_id}/records", data=records)

    def get_record(self, zone_id: str, record_id: str) -> PyonosResponse:
        """Returns the record from the customer zone with the mentioned id.

        Args:
            zone_id (str): The id of the customer zone.
            record_id (str): The id of the record.

        Returns:
            PyonosResponse
        """
        return self._request("GET", f"/zones/{zone_id}/records/{record_id}")

    def delete_record(self, zone_id: str, record_id: str) -> PyonosResponse:
        """Delete a record from the customer zone.

        Args:
            zone_id (str): The id of the customer zone.
            record_id (str): The id of the record.

        Returns:
            PyonosResponse
        """
        return self._request("DELETE", f"/zones/{zone_id}/records/{record_id}")
    
    def put_record(self, zone_id: str, record_id: str, record: dict) -> PyonosResponse:
        """Update a record from the customer zone.

        Args:
            zone_id (str): The id of the customer zone.
            record_id (str): The id of the record.
            record (dict): Updated record.

        Returns:
            PyonosResponse
        """
        return self._request("PUT", f"/zones/{zone_id}/records/{record_id}", data=record)

    # Dynamic DNS
    def post_dyndns(self, data: dict) -> tuple:
        """Activate Dynamic Dns for a bundle of (sub)domains. The url from response will be used to update the ips of the (sub)domains. The following quota applies: 2 requests per minute per IP address.

        Args:
            data (dict): Dynamic Dns configuration.

        Returns:
            PyonosResponse
        """
        return self._request("POST", "/dyndns", data=data)

    def delete_dyndns(self) -> tuple:
        """Disable Dynamic Dns. The following quota applies: 2 requests per minute per IP address.

        Returns:
            PyonosResponse
        """
        return self._request("DELETE", "/dyndns")
    
    def put_dyndns(self, bulk_id: str, data: dict) -> PyonosResponse:
        """Update Dynamic Dns for bulk id. The following quota applies: 2 requests per minute per IP address.

        Args:
            bulk_id (str): Dynamic Dns configuration identifier.
            data (dict): Dynamic Dns configuration.

        Returns:
            PyonosResponse
        """
        return self._request("PUT", f"/dyndns/{bulk_id}", data=data)

    def delete_dyndns_bulk(self, bulk_id: str) -> PyonosResponse:
        """Disable Dynamic Dns for bulk id. The following quota applies: 2 requests per minute per IP address.

        Args:
            bulk_id (str): Dynamic Dns configuration identifier.

        Returns:
            PyonosResponse
        """
        return self._request("DELETE", f"/dyndns/{bulk_id}")


if __name__ == "__main__":
    from pprint import pprint
    dns = Dns("cbad9ce9a7494715b910c560afbe532f", "NvoLcf3uQsnLCttl3MrMZBbY9Y8QsrFayU8srf7lQkrjGvLzenwDp0ZhPPnx_fn042d6Rez3_tu71CiKuC7YFQ")
    zones = dns.get_zones()
    zone_id = zones.json[0]["id"]

    new_record = [
        {
            "name": "cuminsi.de",
            "type": "A",
            "content": "1.2.3.147",
            "ttl": 3600,
            "prio": 0,
            "disabled": False
        }
    ]

    print(dns.post_records(zone_id, new_record))
    print(dns.get_zone(zone_id, record_type="A"))
