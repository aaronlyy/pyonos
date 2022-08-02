
<p align="center">
  <img src=".\media\logo.png" alt="banner" width=65%>
</p>

<h3 align="center"> Wrapper around the IONOS DNS, Domains & SSL API</h3>


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

```py
from pyonos import Dns, Domains, Ssl
```

Similary every API endpoint has its own corresponding method. Here are some of them.

### Info

Every class needs to be autheticated using a [prefix and a secret](https://developer.hosting.ionos.de/keys).

### ionos.Dns

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

## Available methods/endpoints

- Dns
  - get_zones
  - get_zone
  - patch_zone
  - put_zone

## About

Made with ♥ by [aaronlyy](https://github.com/aaronlyy) for [krotesq](https://github.com/krotesq)
