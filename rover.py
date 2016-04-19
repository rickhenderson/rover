""" rover.py
	Module to store functions to control an autonomous rover.
	Created by: Rick Henderson
	Created on: April 18, 2016
	
	Notes:
	April 18, 2016
	* Added clean up routine because GPIO isn't exposed in 
          user programs.
	* Turns OK on smooth surface. Use 1 sec for 90 degree turn.
        * Will buy Pi Servo Hat since Pi has inaccurate PWM signals 
          which could be causing the problem.

	Updated April 18, 2016:
	Pin 7 controls right motors in forward direction
	Pin 11 - right backward

	Pin 15 - Left side motors forward
	Pin 13 - Right side motors backwards
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

def turnRight( intTime ):
	# Try 0.97 seconds for 90 degree turn
	print("Turning right...")
	GPIO.output(7, True)
	GPIO.output(13, True)

	# Sleep the processor so the motors continue to turn.
	time.sleep(intTime)
	# Set the pins to false to stop.
	GPIO.output(7, False)
	GPIO.output(13, False)

	return;

def turnLeft( intTime ):
	# Try 0.97 seconds for 90 degree turn
	print("Turning left...")
	GPIO.output(11, True)
	GPIO.output(15, True)

	# Sleep the processor so the motors continue to turn.
	time.sleep(intTime)
	# Set the pins to false to stop.
	GPIO.output(11, False)
	GPIO.output(15, False)

	return;

def cleanup():
	GPIO.cleanup()

