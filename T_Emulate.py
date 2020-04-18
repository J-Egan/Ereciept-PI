import os
import signal
import subprocess
import time

process = subprocess.Popen(['./nfc-emulate', '-u'],stdout=subprocess.PIPE, universal_newlines=True)

while True:
    status = process.poll()
    print(status)
    # line = process.stdout.readline()
    if status is not None:
        line = process.stdout.read()
        print(line)
        if "userID:" in line:
            startOf = line.find("userID")
            userID = line[startOf:]
            print(userID)
        else:
            print("No UserID detected!")