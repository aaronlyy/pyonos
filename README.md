
<p align="center">
  <img src=".\media\logo.png" alt="banner" width=65%>
</p>

<h3 align="center"> Wrapper around the IONOS DNS, Domains & SSL API</h3>

<p align="center">
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/aaronlyy/pyonos?style=flat">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/aaronlyy/pyonos?style=flat">
  <img alt="GitHub" src="https://img.shields.io/github/license/aaronlyy/pyonos?style=flat">
</p>

## Installation

Pyonos is a PyPi package and can be installed using pip.

```
pip install pyonos
```

## Features

- Full DNS, Domains & SSL API coverage
- Top-Level methods for easier use of the core methods
- DynDns Update Function

## Quickstart

IONOS exposes [3 different API's](https://developer.hosting.ionos.de/docs).

- Dns
- Domains
- Ssl

Every API has its corresponding & same name class that can be imported from pyonos.
Every class needs to be authenticated using a [prefix and a secret](https://developer.hosting.ionos.de/keys).

Similarly, every API endpoint has its own corresponding method. Methods always return a PyonosResponse object which has two properties:

- __.status_code__: The http status code returned
- __.json__: the json response (if not available: None)

### DNS API

[Full IONOS DNS Documentation](https://developer.hosting.ionos.de/docs/dns)

Start by importing the __Dns__ class from pyonos.

```py
from pyonos import Dns
```

Now we need to authenticate with a prefix and a secret.

```py
from pyonos import Dns

dns = Dns("abc", "def")
```

Now we use the __.get_zones()__ method to get all zones available.
Because __PyonosResponse__ overwrites it's \__str__ method, we can just print the response.

```py
from pyonos import Dns

dns = Dns("abc", "def")
response = dns.get_zones()

print(response)

# get single properties like this:
#   response.status_code
#   response.json
```

## List of all available methods/endpoints

Method names are a combination of the http method used and their category.

- Dns ([Official API Docs](https://developer.hosting.ionos.de/docs/dns))
  - Zones
    - get_zones: Returns list of customer zones.
    - get_zone: Returns a customer zone.
    - patch_zone: Replaces all records of the same name and type with the ones provided.
    - put_zone: Replaces all records in the zone with the ones provided.
  - Records
    - post_records: Creates records for a customer zone.
    - get_record: Returns the record from the customer zone with the mentioned id.
    - delete_record: Delete a record from the customer zone.
    - put_record: Update a record from the customer zone.
  - DynDns
    - post_dyndns: Activate dyndns for a group of domains.
    - delete_dyndns: Disable Dynamic Dns.
    - put_dyndns: Update Dynamic Dns for bulk id.
    - delete_dyndns_bulk: Disable Dynamic Dns for bulk id.

## About

Made with ♥ by [aaronlyy](https://github.com/aaronlyy)

## License

[GNU GPL v3](./LICENSE)
