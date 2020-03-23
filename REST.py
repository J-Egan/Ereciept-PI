import requests

URL = "http://54.93.224.148/TAG"

tagData = "This is a test from pi"

PARAMS = {"data":tagData}

r = requests.post(url = URL, data = PARAMS)
