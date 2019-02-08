#!/usr/bin/env python
import requests


#HTTP GET request
r = requests.get('http://ec2-54-191-220-106.us-west-2.compute.amazonaws.com/')

#display html
print(r.text)

#display headers
print(r.headers)