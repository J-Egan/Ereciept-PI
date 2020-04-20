import time
import REST
import subprocess



# Run a constant cycle of checking for new recipets to process
while True:
    # Ping webserver for new reciept
    request = REST.checkTranmission()
    if request.status_code == 200:
        # A new reciept has been found!
        data = request.json()
        recipetID = data['recieptID']

        # Scan NFC for connection
        # Declare Var
        userID = ""
        
        # Run a sub program to access the NFC inteface and enable
        # Emulator mode
        process = subprocess.Popen(['./nfc-emulate'],stdout=subprocess.PIPE, universal_newlines=True)
        
        # Get current subprocess status - Make sure it has not finished yet
        status = process.poll()

        
        while status is None:
            # Check the subprocess current runnning status
            status = process.poll()

            # Check to make sure that the subprogram has finsihed runnning
            # This indicates that an NFC transmission has been detected
            if status is not None:
                #Read information from the subprocess
                line = process.stdout.read()
                # Scan the output for the correct data
                if "userID:" in line:
                    # Parse the userID from the NFC tranmission
                    startOf = line.find(":")
                    userID = line[startOf+1:]       
        time.sleep(2)

        #Combine results and send to webservice
        REST.linkReciept(userID, recipetID)

    time.sleep(5)