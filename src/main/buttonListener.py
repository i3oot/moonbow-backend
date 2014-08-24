import Adafruit_BBIO.GPIO as GPIO
from player import play

buttonPin = "P8_19"
GPIO.setup(buttonPin, GPIO.IN)

while(True):
	GPIO.wait_for_edge(buttonPin, GPIO.RISING)
	play()
