from requests import api

import time

r = api.get('https://fabrykatestow.pl')
time.sleep(5)
print(r.status_code)
time.sleep(5)
print(r.headers['content-type'])
time.sleep(1)
print(r.encoding)
time.sleep(1)
print(r.json)