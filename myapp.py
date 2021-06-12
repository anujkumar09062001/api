import requests

URL = 'http://127.0.0.1:8000/studetail/2'

r = requests.get(url= URL)

print(r.json())