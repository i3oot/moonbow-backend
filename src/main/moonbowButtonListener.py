import Adafruit_BBIO.GPIO as GPIO
from moonbowPlayer import play

buttonPin = "P8_14"
GPIO.setup(buttonPin, GPIO.IN)

while(True):
	GPIO.wait_for_edge(buttonPin, GPIO.RISING)
	play()
