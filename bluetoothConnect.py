import os

speakerAddress = "08:EB:ED:DA:7E:5C"                       #paste device address here


os.system('bluetoothctl connect {}'.format(speakerAddress))

