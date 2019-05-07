Example code of creating an email account
======

```python
import requests

auth = ('admin', '2c3TKBY+')

data = {'email': 'email@ciimbre.com', 'password': 'new_password'}

response = requests.post(
    'https://mail-api.ciimbre.com/accounts/',
    auth=auth, data=data
)
```
