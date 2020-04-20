import REST
import time

while True:
    r = REST.checkTranmission()
    if r.status_code == 200:
        data = r.json()
        recipetID = data['recieptID']
        REST.linkReciept(1, recipetID)
    else:
        print("No reciepts availble")
    time.sleep(5)