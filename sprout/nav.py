""" nav.py
        * usage: sudo python3 nav.py

	Program to move Sprout interactively.
	Created by: Rick Henderson
	Created on: May 16, 2016
	
	Notes:
	May 16, 2016
"""

import time
import sys

# Import the functions specific to controlling the Rover
import rover as rover

# Main ###################################

print("\n****** Sprout here! Ready for action!\n")
print("Type QUIT or quit to exit.\n")

# Start the loop
print("Commands are: f, b, r, l, and spin.")
cmd = input("Enter a direction: ")

# Make commands case-insensitive
#cmd = lower(cmd)

while cmd != "quit":
	if cmd == "f":
		rover.moveForward(2)
	elif cmd == "b":
		rover.moveBackward(2)
	elif cmd == "r":
		rover.turnRight(0.97)
	elif cmd == "l":
		rover.turnLeft(0.97)
	elif cmd == "spin":
		rover.turnLeft(4)
	else:
		print("Sprout: 'I did not understand that!'")
		cmd = "quit"

	cmd = input("Enter a direction: ")	

# Delay then clean up
time.sleep(1)
rover.cleanup()
