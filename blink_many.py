# Working with Raspberry Pi and a breadboard
# Started: September 14, 2015
# Modified: September 15, 2015
# Written by: Rick Henderson

# Note: Must be in sudo mode to work with GPIO pins

# Wiring the breadboard:
# Jumper Pin 7 on GPIO to first row on the breadboard
# Pin 6: Grnd or negative
# Resistor goes on negative side of LED, power goes to positive.

import RPi.GPIO as GPIO
import time

# Use variables to customize how this program runs.
# Placing the variables here means the next programmer
#   doesn't have to look through a lot of code to make
#   simple changes.

REPETITIONS = 5	# Number of reps of the entire cycle
BLINKS = 3	# Number of time the LED blinks in one rep
LONG_DELAY = 1  # Amount of time (in seconds) between reps
SHORT_DELAY = 0.25 # Amount of time (in seconds) between blinks

# Set the Pin numbering mode
GPIO.setmode(GPIO.BOARD) # Simplest

# Set pin 7 for output (this provides 3.7V power)
GPIO.setup(7, GPIO.OUT)  # Can use 8 different pins for output.

# Set a loop for repetitions of the short blink sequence
for reps in range(0, REPETITIONS):
	# Turn the LED on 3 times.
	for blink in range(0, BLINKS):
		GPIO.output(7, True)
		# Sleep/pause/wait for 1 second
		time.sleep(SHORT_DELAY)
		GPIO.output(7, False)
		time.sleep(SHORT_DELAY)
	# Now a complete rep is done, start again after a long delay.
	time.sleep(LONG_DELAY)

GPIO.cleanup()

