# __init__.py

from api import Dns
# from domains import Domains
# from ssl import Ssl

if __name__ == "__main__":
    from os.path import exists
    from pprint import pprint
    if exists("./ionos/config.py"):
        from config import PREFIX, SECRET

        dns = Dns(PREFIX, SECRET)
        pprint(dns.get_zones())

    else:
        print("missing config.py")