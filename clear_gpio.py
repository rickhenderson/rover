# A simple program to clear the GPIO pins
#   when a program is interrupted before
#   a clean finish.
import RPi.GPIO as GPIO
GPIO.cleanup()


