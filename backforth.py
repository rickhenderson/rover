""" backforth.py
        * usage: sudo python backforth.py <nreps>

	Program to move the rover forward and backwards a 
        specified number of times.

	Created by: Rick Henderson
	Created on: April 18, 2016
	
	Notes:
	April 18, 2016
        * Added command line arguments for number of repetitions.
          * usage: sudo python backforth.py <nreps>
	* Condensed movement functions into rover.py module
	* Turns OK on smooth surface. Use 1 sec for 90 degree turn.
        * Will buy Pi Servo Hat since Pi has inaccurate PWM signals 
          which could be causing the problem.

"""

import time
import sys

# Import the functions specific to controlling the Rover
import rover as rover

# Main ###################################

# Get the number of repetitions from the command line
# Can use argparse for more control, including usage commnds
reps = int(sys.argv[1])

print("Rover: '8 second delay. Get the camera ready!'")
time.sleep(8)

# Start the loop
for i in range(reps):
	rover.moveForward(2)
	time.sleep(0.5)
	rover.moveBackward(2)
	time.sleep(0.5)

# Delay then clean up
time.sleep(1)
rover.cleanup()
