import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
inputPin = 40
outputPin = 38
GPIO.setup(inputPin,GPIO.IN)
GPIO.setup(outputPin,GPIO.OUT)

inputState = 0
prevInputState = 0

outputState = 0

try:
	while True:
		print(inputState,outputState)
		inputState = GPIO.input(inputPin)
		if inputState != prevInputState:
			if inputState == 1:
				outputState = not outputState
				GPIO.output(outputPin,outputState)
		prevInputState = inputState
except KeyboardInterrupt:
	GPIO.cleanup()		
