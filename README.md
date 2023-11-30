Example code of creating an email account
======

virtualenv -p python3.10 venv
source venv/bin/activate
pip install -r requirements.txt


```python
import requests

auth = ('admin', '2c3TKBY+')

data = {'email': 'email@ciimbre.com', 'password': 'new_password'}

response = requests.post(
    'https://mail-api.ciimbre.com/accounts/',
    auth=auth, data=data
)
```
