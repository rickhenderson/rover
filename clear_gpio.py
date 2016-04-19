# A simple program to clear the GPIO pins
#   when a program is interrupted before
#   a clean finish.
import RPi.GPIO as GPIO

# Set mode and output pins */
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# Hide any warnings
GPIO.setwarnings(False)

# Clear the pins
GPIO.cleanup()


