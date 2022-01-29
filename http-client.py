#!/usr/bin/env python
#Simple python web client

import sys
import requests

try:
    x = sys.argv[1]
    if x.startswith('http://') or x.startswith('https://'):
        x = x
    else:
        x = ('http://' + x)
    res = requests.get(x)
except IndexError:
    print('usage: web-client.py <HOST>')
    sys.exit(1)
except requests.exceptions.MissingSchema:
    print('There is something wrong with url format')
except requests.exceptions.ConnectionError:
    x = x.replace("http://","")
    print('Failed to establish connection to ' + x)
else:
    print(res.text)

