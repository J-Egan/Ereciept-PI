import requests

def sendPost(tagData):
    URL = "http://54.93.224.148/TAG/upload"
    PARAMS = {'data':tagData}
    r = requests.post(url = URL, data = PARAMS)

sendPost("This is a test function call from pi")
sendPost("Raspberry PI")
