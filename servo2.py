# Courtesy of Gaven MacDonald on Youtube
# Using a servo requires PWM - Pulse Width Modulation
# Required are some calculations re: Duty Cycle which
# have been integrated into the code.

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

# Set up PWM
p = GPIO.PWM(7,50)
p.start(7.5) # Neutral

try:
	while True:
		p.ChangeDutyCycle(7.5) # Neutral
		time.sleep(1)

		p.ChangeDutyCycle(12.5) # 180 Deg
		time.sleep(1)

		p.ChangeDutyCycle(2.5) # 0 Deg
		time.sleep(1)

# Keep looping until a key is pressed.
except KeyboardInterrupt:
	# Stop PWM mode
	p.stop()

	GPIO.cleanup()

