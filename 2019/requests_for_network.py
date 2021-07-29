import requests, pprint 

res = requests.get('http://httpbin.org/get')
pprint.pprint(res.json())
