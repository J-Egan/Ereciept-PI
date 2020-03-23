import nxppy
import time
import ndef
import REST

mifare = nxppy.Mifare()

# Print card UIDs as they are detected
while True:
    try:
        uid = mifare.select()
        print(uid)
        ndef_data = mifare.read_ndef()
        print(ndef_data)
        # Parse NDEF data
        ndef_records = list(ndef.message_decoder(ndef_data))

        tagData = "UID: " + uid + " | NDEF: "

        # for x in ndef_records:
        #     print(x)
        #     tagData = tagData + str(x) + " "

        print(tagData)
        REST.sendPost(tagData)

    except nxppy.SelectError:
        # SelectError is raised if no card is in the field.
        pass

    time.sleep(1)
