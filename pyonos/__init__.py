# __init__.py

from api import Dns
import json
# from domains import Domains
# from ssl import Ssl

if __name__ == "__main__":
    from os.path import exists
    from pprint import pprint
    if exists("./pyonos/config.py"):
        from config import PREFIX, SECRET

        records = [
            {
                "name": "cuminsi.de",
                "type": "TXT",
                "content": "hallo",
                "ttl": 3600,
                "prio": 0,
                "disabled": False
            }
        ]

        record = {
                "name": "cuminsi.de",
                "type": "TXT",
                "content": "by7984375e",
                "ttl": 3600,
                "prio": 0,
                "disabled": False
            }

        dns = Dns(PREFIX, SECRET)
        zone_id = dns.get_zones()[1][0]["id"]
        record_id = dns.get_zone(zone_id)[1]["records"][0]["id"]
        # pprint(dns.post_records(zone_id, records))
        pprint(dns.put_record(zone_id, record_id, record))

    else:
        print("missing config.py")