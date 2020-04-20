import requests
import fileIO

def sendPost(tagData):
    print("Attempting to send: " + tagData)
    URL = "http://54.93.224.148/TAG/upload"
    PARAMS = {'data':tagData}
    requests.post(url = URL, data = PARAMS)

def checkTranmission():
    PIREF = fileIO.getContents("ref.txt")
    URL= fileIO.getContents("url_CheckTransmission.txt")
    PARAMS = {'id':PIREF}
    r = requests.get(URL, PARAMS)
    return r

def linkReciept(userID, recieptID):
    URL= fileIO.getContents("url_LinkReciept.txt")
    PARAMS = {'userID': userID,
              'recieptID': recieptID}
    # Send POST request to webservice
    requests.post(URL, PARAMS)
