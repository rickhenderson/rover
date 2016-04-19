""" turntest.py
	Program to test making the rover turn from a Raspberry Pi.
	Created by: Rick Henderson
	Created on: April 18, 2016

	April 18:
        * Won't turn on carpet, will turn on smooth floor but slowly.
	* Left and right pins below may be reversed.
	* Turning for 10 seconds is probably more than 360 degrees
          when it begins working.
        * Turning for 1 second = 90 degree turn given current status.
	* Will buy a Pi servo Hat from Adafruit as Pi has problems with
          accurate PWM signals. This could be the reason.

	Notes from  Nov 7, 2015:
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

# Main ##########################################
turnRight(2)

# Delay then clean up
time.sleep(1)
GPIO.cleanup()
