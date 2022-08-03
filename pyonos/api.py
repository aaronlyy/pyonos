import requests

class Dns:
    def __init__(self, prefix: str, secret: str) -> None:
        self._base = "https://api.hosting.ionos.com/dns/v1"
        self._headers = {"X-API-KEY": f"{prefix}.{secret}"}

    def _request(self, method: str, endpoint: str, params: dict = None, data: list = None) -> tuple:
        method = method.lower()
        url = f"{self._base}{endpoint}"

        if method == "get":
            response = requests.get(url, params=params, headers=self._headers)
            return (response.status_code, response.json())

        elif method == "patch":
            response = requests.patch(url, json=data, headers=self._headers)
            if response.status_code == 200:
                return (response.status_code, None)
            else:
                return (response.status_code, response.json())

        elif method == "put":
            response = requests.put(url, json=data, headers=self._headers)
            if response.status_code == 200:
                return (response.status_code, None)
            else:
                return (response.status_code, response.json())
        
        elif method == "post":
            response = requests.post(url, json=data, headers=self._headers)
            return (response.status_code, response.json())

        elif method == "delete":
            response = requests.delete(url, headers=self._headers)
            if response.status_code == 200:
                return (response.status_code, None)
            else:
                return (response.status_code, response.json())

        else:
            return (None, None)

    # --- ZONES ---
    def get_zones(self) -> tuple:
        """Returns list of customer zones.

        Returns:
            tuple: (status_code, json)
        """
        return self._request("GET", "/zones")

    def get_zone(self, zone_id: str, suffix: str = None, record_name: str = None, record_type: str = None) -> tuple:
        """Returns a customer zone.

        Args:
            zone_id (str)
            suffix (str, optional): The FQDN used to filter all the record names that end with it.
            record_name (str, optional): The record names that should be included (same as name field of Record).
            record_type (str, optional): A comma-separated list of record types that should be included.

        Returns:
            tuple: (status_code, json)
        """
        params = {
            "suffix": suffix,
            "recordName": record_name,
            "recordType": record_type
        }
        return self._request("GET", f"/zones/{zone_id}", params=params)

    def patch_zone(self, zone_id: int, records: list) -> tuple:
        """Replaces all records of the same name and type with the ones provided.

        Args:
            zone_id (int)
            data (list)

        Returns:
            tuple: (status_code, None) [200]
        """
        return self._request("PATCH", f"/zones/{zone_id}", data=records)

    def put_zone(self, zone_id: int, records: list) -> tuple:
        """Replaces all records in the zone with the ones provided.

        Args:
            zone_id (int)
            data (list)

        Returns:
            tuple: (status_code, None) [200]
        """
        return self._request("PUT", f"/zones/{zone_id}", data=records)

    # --- RECORDS ---
    def post_records(self, zone_id: str, records: list) -> tuple:
        """Creates records for a customer zone.

        Args:
            zone_id (str)
            records (list): List of record dictionaries

        Returns:
            tuple: (status_code, json) [201]
        """
        return self._request("POST", f"/zones/{zone_id}/records", data=records)

    def get_record(self, zone_id: str, record_id: str) -> tuple:
        """Returns the record from the customer zone with the mentioned id.

        Args:
            zone_id (str): The id of the customer zone.
            record_id (str): The id of the record.

        Returns:
            tuple: (status_code, json)
        """
        return self._request("GET", f"/zones/{zone_id}/records/{record_id}")

    def delete_record(self, zone_id: str, record_id: str) -> tuple:
        """Delete a record from the customer zone.

        Args:
            zone_id (str): The id of the customer zone.
            record_id (str): The id of the record.

        Returns:
            tuple: The id of the record.
        """
        return self._request("DELETE", f"/zones/{zone_id}/records/{record_id}")
    
    def put_record(self, zone_id: str, record_id: str, record: dict) -> tuple:
        """Update a record from the customer zone.

        Args:
            zone_id (str): The id of the customer zone.
            record_id (str): The id of the record.
            record (dict): Updated record.

        Returns:
            tuple: (status_code, json)
        """
        return self._request("PUT", f"/zones/{zone_id}/records/{record_id}", data=record)

    # Dynamic DNS
    def post_dyndns(self, data: dict) -> tuple:
        """Activate Dynamic Dns for a bundle of (sub)domains. The url from response will be used to update the ips of the (sub)domains. The following quota applies: 2 requests per minute per IP address.

        Args:
            data (dict): Dictionary containing domains & description

        Returns:
            tuple: (status_code, json)
        """
        return self._request("POST", "/dyndns", data=data)
