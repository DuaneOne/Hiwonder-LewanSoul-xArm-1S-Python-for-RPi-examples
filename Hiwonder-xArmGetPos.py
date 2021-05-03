"""
This Python3 script runs on a raspberry pi with HiWonder xArm-1S robot arm attached from
any pi usb port to xArm controller micro-usb port.

Each arm Sequence list is obtained by manually moving the arm to the desired position,
running this script, then copying the print output into another script which will
move the arm. Then move the arm to a new position and run the script again.  Repeat
as many sequence positions as needed.  The print output from one run of the script
starts with servo1 and ends with servo6, looks like this :   [277, 497, 495, 545, 499, 489]
"""

import xarm                    # to control the robot arm     https://github.com/ccourson/xArmServoController

arm = xarm.Controller('USB')   # usb cable from any pi usb port to arm controller micro-usb port


# Prints the position of all servos in units ( or replace False with True for degrees)
position = []
for i in range (1,7):
    position.append(arm.getPosition(i, False))
print(position)

arm.servoOff()                # Turns off all servo motors