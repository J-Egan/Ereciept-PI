import subprocess
import time

process = subprocess.Popen(['./nfc-emulate'],stdout=subprocess.PIPE, universal_newlines=True)

while True:
    status = process.poll()
    print(status)
    # line = process.stdout.readline()
    if status is not None:
        line = process.stdout.read()
        print(line)
        if "userID:" in line:
            startOf = line.find(":")
            userID = line[startOf+1:]
            print(userID)
            exit()
        else:
            print("No UserID detected!")
    time.sleep(3)