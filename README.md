
<p align="center">
  <img src=".\media\logo.png" alt="banner" width=65%>
</p>

<h3 align="center"> Wrapper around the IONOS DNS, Domains & SSL API</h3>

![GitHub](https://img.shields.io/github/license/aaronlyy/pyonos?style=flat-square)


## Installation

### Install using pip

```
pip install pyonos
```

### Clone the repository

```
git clone https://github.com/aaronlyy/pyonos
```

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

[IONOS DNS Documentation](https://developer.hosting.ionos.de/docs/dns)

#### .get_zones() : Get all available zones.

```py
from pyonos import Dns
from pprint import pprint

dns = Dns("prefix", "secret")
result = dns.get_zones()

pprint(result)

```

### pyonos.Domains (WORK IN PROGRESS)

### pyonos.Ssl (WORK IN PROGRESS)

## Currently supported methods/endpoints

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

## About

Made with ♥ by [aaronlyy](https://github.com/aaronlyy)
