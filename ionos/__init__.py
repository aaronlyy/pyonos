# __init__.py

from dns import Dns
# from domains import Domains
# from ssl import Ssl

if __name__ == "__main__":
    from os.path import exists
    if exists("./ionos/config.py"):
        from config import PREFIX, SECRET

        dns = Dns(PREFIX, SECRET)
        dns.get_zones()

    else:
        print("missing config.py")