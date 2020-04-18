import os
import signal
import subprocess

process = subprocess.Popen(['explorenfc-cardemulation'],stdout=subprocess.PIPE, universal_newlines=True)

while True:
    print(process.poll())
    line = process.poll()
    # line = process.stdout.readline()
    print(line)
    if "userID:" in line:
        startOf = line.find("userID")
        userID = line[startOf:]
        print(userID)

        # Kill subprocess now
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    else:
        print("No UserID detected!")
