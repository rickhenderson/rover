""" square2.py
	Program to move Rover in a small square suitable for small areas.
	Created by: Rick Henderson
	Created on: April 18, 2016
	
	Notes:
	April 18, 2016
	* Turns OK on smooth surface. Use 1 sec for 90 degree turn.
        * Will buy Pi Servo Hat since Pi has inaccurate PWM signals 
          which could be causing the problem.
	* The Left/Right description below is probably backwards.

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


# Main ##########################################
time.sleep(5)




# Move in a square!
moveForward(2)
turnLeft(2)
moveForward(2)
turnLeft(1)
moveForward(2)
turnLeft(1)
moveForward(2)
turnLeft(1)

# Move Backwards for 3 seconds
moveBackward(2)
print("Square completed.")

# Delay then clean up
time.sleep(1)
GPIO.cleanup()
