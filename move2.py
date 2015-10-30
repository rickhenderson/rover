""" move2.py
	Program to control motors on a bot from a Raspberry Pi.
	Created by: Rick Henderson
	Created on: October 19, 2015
	Code from: https://youtu.be/AZSiqj0NZgU
	Updated: October 25, 2015
		- Modifed to make it move forward for 2 seconds
		- and then backwards.
	Updated: October 29, 2015
		- Modified it to use functions for moving backward and forward
		- after getting 4 motors to run
	Pins 7&11 control left back and left front motors.
	Pins 13&15 control right back and right front motors.
"""

import RPi.GPIO as GPIO
import time

# Set mode and output pins */
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

def moveForward( intTime ):
	" Move the rover forward for intTime seconds."
	# Set and a signal 
	# To drive motor forward, set pins 7 and 15 to True.
	print("Moving forward...")
	GPIO.output(7, True)
	GPIO.output(15, True)
	# Sleep the processor so the motors continue to turn.
	time.sleep(intTime)
	# Set the pins to false to stop.
	GPIO.output(7, False)
	GPIO.output(15, False)
	return;

def moveBackward( intTime ):
	"This function moves the rover backwards for intTime seconds."	
	print("Moving backward...")
	GPIO.output(11, True)
	GPIO.output(13, True)
	# Sleep during duration of move
	time.sleep(intTime)
	# Set the outputs to false to stop motors
	GPIO.output(11, False)
	GPIO.output(13, False)
	return;

# Main ##########################################
# Move forward for 2 seconds
moveForward(2)
# Move Backwards for 2 seconds
moveBackward(2)

# Delay then clean up
time.sleep(1)
GPIO.cleanup()



