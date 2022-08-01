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

        record ={
                "name": "cuminsi.de",
                "type": "A",
                "content": "1.1.1.4",
                "ttl": 3600,
                "prio": 0,
                "disabled": False
            }

        pprint(dns.patch_zone(zone_id, data=record))

    else:
        print("missing config.py")