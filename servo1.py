# Courtesy of Gaven MacDonald on Youtube
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

try:
	while True:
		GPIO.output(7,True)
		# Modifiy the duration to set servo to neutral
		# 0.0015s for Gaven's servo
		# Clockwise rotation should be fine for HiTec HS-422
		time.sleep(0.0015)
		GPIO.output(7,False)

		time.sleep(2)

# Keep looping until a key is pressed.
except KeyboardInterrupt:
	GPIO.cleanup()

