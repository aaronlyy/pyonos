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

        dns = Dns(PREFIX, SECRET)
        zone_id = dns.get_zones()[1][0]["id"]
        print(zone_id)

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

        # pprint(dns.patch_zone(zone_id, data=record))

        pprint(dns.post_records(zone_id,records=records))


    else:
        print("missing config.py")