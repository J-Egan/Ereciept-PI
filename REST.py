import requests

def sendPost(tagData):
    print("Attempting to send: " + tagData)
    URL = "http://54.93.224.148/TAG/upload"
    PARAMS = {'data':tagData}
    r = requests.post(url = URL, data = PARAMS)
