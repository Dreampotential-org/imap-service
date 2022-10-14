import requests

auth = ('admin', '2c3TKBY+')

data = {'email': 'anna@agentstat.com', 'password': 'new_password'}

response = requests.post(
        'http://127.0.0.1:8000/accounts/', auth=auth, data=data
)
