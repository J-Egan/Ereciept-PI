import nxppy
import time
import ndef
import REST

mifare = nxppy.Mifare()

# Print card UIDs as they are detected
while True:
    try:
        REST.checkTranmission()
    except nxppy.SelectError:
        # SelectError is raised if no card is in the field.
        pass

    time.sleep(1)
