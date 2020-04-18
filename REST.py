import requests
import fileIO

def sendPost(tagData):
    print("Attempting to send: " + tagData)
    URL = "http://54.93.224.148/TAG/upload"
    PARAMS = {'data':tagData}
    r = requests.post(url = URL, data = PARAMS)

def checkTranmission():
    print("Attemption to Check for Transmission")
    URL="http://192.168.1.10/EReciept/index.php/pos/checkTransmission"
    PARAMS = {'id':fileIO.getREF()}
    r = requests.get(url = URL, data = PARAMS)
    print(r)
