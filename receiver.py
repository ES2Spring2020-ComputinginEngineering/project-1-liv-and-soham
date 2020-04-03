##################
# FILL IN HEADER
#################

import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=3, length =100)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)


# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
print('start')


while True:
    incoming = radio.receive() # Read from radio

    if incoming is not None: # message was received
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)
        newmessage = incoming.split('/')
        newtuple = (int(newmessage[0]), int(newmessage[1]), int(newmessage[2]), int(newmessage[3]))
        print(newtuple)
        #############################################################
        # FILL IN HERE
        # Incoming is string sent from logger
        # Need to parse it and reformat as a tuple for the MU plotter
        #############################################################

        mb.sleep(10)