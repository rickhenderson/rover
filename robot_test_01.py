/* robot_test_01.py
	Program to test and control motors from Raspberry Pi.
	Created by: Rick Henderson
	Created on: October 19, 2015
	Code from: https://youtu.be/AZSiqj0NZgU
	Pins 7&11 control motor 1.
	Pins 13&15 control motor 2. 
	The following program will test the motors
		by turning it one direction then the other.
		In this program, other motor doesn't turn while one is
		turning the robot.
*/

import RPi.GPIO as GPIO
import time

/* Set mode and output pins */
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

/* Set and a signal */
/* To drive motor forward, set pins 7 and 13 to True. */
print("Turning one direction...")
GPIO.output(7, True)
time.sleep(1)
print("Turning the other direction..."
GPIO.output(7, False)
GPIO.output(11, True)
time.sleep(1)
GPIO.output(11, False)
GPIO.output(13, True)
time.sleep(1)
GPIO.output(13, False)
GPIO.output(15, True)
time.sleep(1)
GPIO.output(15, False)
GPIO.cleanup()



