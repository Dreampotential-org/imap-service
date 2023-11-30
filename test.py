import requests

auth = ('root', '2c3TKBY+')
data = {'email': 'adem@agentstat.com', 'password': 'password'}
response = requests.post(
    'http://127.0.0.1:8833/accounts/', auth=auth, data=data
)
data = {'email': 'anna@agentstat.com', 'password': 'new_password'}
response = requests.post(
    'http://127.0.0.1:8833/accounts/', auth=auth, data=data
)
