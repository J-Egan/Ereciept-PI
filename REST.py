import requests

URL = "54.93.224.148/TAG/upload"

tagData = "This is a test from pi"

PARAMS = {'data':tagData}

r = requests.post(url = URL, data = PARAMS)
