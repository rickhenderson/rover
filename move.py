""" move.py
	Program to control motors on a bot from a Raspberry Pi.
	Created by: Rick Henderson
	Created on: October 19, 2015
	Code from: https://youtu.be/AZSiqj0NZgU
	Updated: October 25, 2015
		- Modifed to make it move forward for 2 seconds
		- and then backwards.
	Pins 7&11 control motor 1.
	Pins 13&15 control motor 2. 
"""

import RPi.GPIO as GPIO
import time

# Set mode and output pins */
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# Set and a signal 
#To drive motor forward, set pins 7 and 15 to True.
print("Moving forward...")
GPIO.output(7, True)
GPIO.output(15, True)
time.sleep(2)
GPIO.output(7, False)
GPIO.output(15, False)

print("Moving backward...")
GPIO.output(11, True)
GPIO.output(13, True)

time.sleep(2)

GPIO.output(11, False)
GPIO.output(13, False)


time.sleep(1)
GPIO.cleanup()



