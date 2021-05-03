# Hiwonder-LewanSoul-xArm-1S-Python-for-RPi-examples
Examples of simple python scripts for the Hiwonder xArm 1S using this library: https://github.com/ccourson/xArmServoController
Requires a single connection from the xArm controller micro usb to any usb port on the RPi.

The idea is the xArm physically moved by hand to the desired position and then the Hiwonder-xArmGetPos script is run to capture all the servo positions.  These can be changed later.

Then Hiwonder-xArmMove is run to perform the moves.   The example is picking up a small piece of wood and lifting it up.  The thickness of the wood can be basically any size that can fit into the gripper.  The following strategy is used for gripping:

Grip claw open all the way

Try to grip the object  all the way closed

Read the actual grip postion

Turn servo off to relieve any backpressure

Grip to the real position; should be no strain on the servo
