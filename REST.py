import requests
import fileIO

def sendPost(tagData):
    print("Attempting to send: " + tagData)
    URL = "http://54.93.224.148/TAG/upload"
    PARAMS = {'data':tagData}
    requests.post(url = URL, data = PARAMS)

def checkTranmission():
    PIREF = fileIO.getREF()
    URL="http://192.168.1.10/EReciept/index.php/pos/checkTransmission"
    PARAMS = {'id':PIREF}
    r = requests.get(URL, PARAMS)
    print(r.url)
    print(r)
    return r
