""" moveturn.py
	Program to control motors on a bot from a Raspberry Pi.
	Created by: Rick Henderson
	Created on: November 7, 2015
		- purchased a Mental Beats battery back for untethered greatness!
		- seems not to have enough power to turn
	Updated Nov 7, 2015:
	Pin 7 controls left motors in forward direction
	Pin 11 - Left backward

	Pin 15 - Right side motors forward
	Pin 13 - right side motors backwards
"""

import RPi.GPIO as GPIO
import time

# Set mode and output pins */
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

### Function definitions

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

def turnLeft( intTime ):
	# Try 0.97 seconds for 90 degree turn
	print("Turning left...")
	GPIO.output(7, True)
	GPIO.output(13, True)

	# Sleep the processor so the motors continue to turn.
	time.sleep(intTime)
	# Set the pins to false to stop.
	GPIO.output(7, False)
	GPIO.output(13, False)

	return;


# Main ##########################################
# Move forward for 5 seconds
moveForward(5)
turnLeft(1)
# Move Backwards for 5 seconds
moveBackward(5)

# Delay then clean up
time.sleep(1)
GPIO.cleanup()


