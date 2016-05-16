""" ru.py
	Rover Utilities for testing pin connections when changing configurations
	User enters a pin number and that pin is activated for 3 seconds then stops.
	Created by: Rick Henderson
	Created on: May 16, 2016
	
	Notes:
	May 16, 2016:
	This program designed so I can test the pin / motor config interactively
	from a console so I can be sure the wiring is correct.
	I moved the RPi B+ and the LN298 board to the 2 wheeled rover and only
	  one tire rotates. Need to check also to see if grnd wire from board
	  should connect to grnd on Pi.
	 
	Pin 7 controls right motor in forward direction
	Pin 11 - right backward
	Pin 15 - Left side motor forward
	Pin 13 - Right side motor backwards
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

def cleanup():
	GPIO.cleanup()

# A list of active pins
active_list = [7, 11, 13, 15]

print("\n***** Interactive Rover Control Utility *****\n")
print("Possible setup: Forward: 7 and 15. Reverse: 11 and 13")
current_pin = int(input("Enter the pin you want to activate. Enter 99 to quit: "))

while current_pin <> 99:
  if current_pin not in active_list:
    print("That pin is currenty not active. Try ", active_list)
  else:  
    print("Activating Pin: {:d}".format(current_pin))
  
    # Activate the pin then sleep for 3 seconds and stop
    GPIO.output(current_pin, True)
    time.sleep(3)
    GPIO.output(current_pin, False)
  
cleanup()
