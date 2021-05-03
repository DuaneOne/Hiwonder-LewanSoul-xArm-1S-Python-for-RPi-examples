"""
This Python3 script runs on a raspberry pi with HiWonder xArm-1S robot arm attached from
any pi usb port to xArm controller micro-usb port.  The code allows the claw gripper to
grip objects of various sizes.

Each arm Sequence is obtained by manually moving the arm to the desired position,
running the following code, then copying the output into this script. Modify the values
as follows.  use a single [value] for servo1 to grip to almost closed position
use 999.9 for servo1 to remain unchanged (useful after gripping to move the rest of the
arm to another location).
        position = []
        for i in range (1,7):        # get all 6 servo positions, starting with servo1
            position.append(arm.getPosition(i, False))  # change to True to get angle in degrees
        print(position)
"""

import xarm               # to control the robot arm     https://github.com/ccourson/xArmServoController
from time import sleep    # use this time for sleep.  this time is different than datetime.time

arm = xarm.Controller('USB')  # usb cable from any pi usb port to arm controller micro-usb port

# Note use your values for armSequence which will likely be different for your xArm
armSequence = [
    [277, 497, 495, 545, 499, 489],       # home, straight up, claw open
    [277, 497, 200, 835, 432, 498],       # down
    [699],                                # grab small wood square
    [999.9, 497, 495, 545, 499, 489]      # home, straight up

]

def moveGripper(pos):
    arm.setPosition(1, pos, 1000, True)    #  try to grip to almost all the way closed,
    pos = arm.getPosition(1)               #  then read the actual grip position.
    arm.servoOff(1)                        #  turn the gripper servo off to relieve any back pressure.
    arm.setPosition(1, pos, 1000, True)    #  grip to real position; should be no strain on servo.
    #print(pos)                            #  for debug you can see how the grip changes with object size.



for s in armSequence:
    if s[0] == 999.9:                      # don't change servo1 (gripper)
        arm.setPosition([[2, s[1]], [3, s[2]], [4, s[3]], [5, s[4]], [6, s[5]]], 2000)
    elif len(s) == 1:
        moveGripper(s[0])
    elif len(s) == 6:
        arm.setPosition( [[1,s[0]], [2,s[1]], [3,s[2]], [4,s[3]], [5,s[4]], [6,s[5]] ], 2000 )
    else:
        print("each list in arm_Sequence must have a length of 1 or 6 ")

    sleep(2)
sleep(3)  # seconds

arm.servoOff()                        #  Turns off all servo motors, could posibly release gripped object


