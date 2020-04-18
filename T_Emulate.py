import os
import signal
import subprocess
import time

process = subprocess.Popen(['explorenfc-cardemulation', '-u'],stdout=subprocess.PIPE, universal_newlines=True)

while True:
    status = process.poll()
    # line = process.stdout.readline()
    if status is not None:
        line = process.stdout.read()
        print(line)
        if "userID:" in line:
            startOf = line.find("userID")
            userID = line[startOf:]
            print(userID)

            # Kill subprocess now
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        else:
            print("No UserID detected!")
    time.sleep(5)