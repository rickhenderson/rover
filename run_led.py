# Working with Raspberry Pi and a breadboard
# Started: September 14, 2015
# Written by: Rick Henderson

# Note: Must be in sudo mode to work with GPIO pins

# Wiring the breadboard:
# Jumper Pin 7 on GPIO to first row on the breadboard
# Pin 6: Grnd or negative
# Resistor goes on negative side of LED, power goes to positive.

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) # Simplest
GPIO.setup(7, GPIO.OUT)  # Can use 8 different pins for output.

for x in range(0,3):
	print("LED On") # GPIO.output(7,True)
	# Sleep/pause/wait for 1 second
	time.sleep(1)
	print("LED Off") # GPIO.output(7,False)
	time.sleep(1)
GPIO.cleanup()

