#!/usr/bin/env python
import requests,json 

url = 'http://ec2-54-191-220-106.us-west-2.compute.amazonaws.com/'
#dictionary
payload = {'name': 'Eliezer', 'message':'this is the message'}
#dictionary automatically form-encoded when the request is made
r = requests.post(url, data=json.dumps(payload))

print(r.text)