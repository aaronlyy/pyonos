
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

### List of available methods/endpoints

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
    - post_dyndns(): Activate dyndns for a group of domains.

## Quickstart

IONOS exposes [3 different API's](https://developer.hosting.ionos.de/docs).

- Dns
- Domains
- Ssl

Every API has its corresponding & same name class that can be imported from pyonos.
Every class needs to be authenticated using a [prefix and a secret](https://developer.hosting.ionos.de/keys).

```py
from pyonos import Dns, Domains, Ssl
```

Similarly, every API endpoint has its own corresponding method. Methods always return a tuple containing two items:

- HTTP Status Code
- JSON Response (if not available: None)

### pyonos.Dns

[Full IONOS DNS Documentation](https://developer.hosting.ionos.de/docs/dns)

Start by importing the Dns class from pyonos.

```py
from pyonos import Dns
```

Now we need to authenticate with a prefix and a secret.

```py
from pyonos import Dns

dns = Dns("abc", "def")
```

Now we use the .get_zones() method and pprint (pretty print) to get all zones.

```py
from pyonos import Dns
from pprint import pprint

dns = Dns("abc", "def")
code, result = dns.get_zones()

if code == 200:
  pprint(result)
else:
  print("error")
```

### pyonos.Domains

Work in progress

### pyonos.Ssl (WORK IN PROGRESS)

Work in progress

## About

Made with ♥ by [aaronlyy](https://github.com/aaronlyy)

## License

[GNU GPL v3](./LICENSE)