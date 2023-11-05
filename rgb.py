import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

redLED = 37
greenLED = 35
blueLED = 33

redButton = 40
greenButton = 38
blueButton = 36

redLEDState = 0
greenLEDState = 0
blueLEDState = 0

redButtState = 0
greenButtState = 0
blueButtState = 0

oldRedButtState = 0
oldGreenButtState = 0
oldBlueButtState = 0

GPIO.setup(redLED, GPIO.OUT)
GPIO.setup(greenLED, GPIO.OUT)
GPIO.setup(blueLED, GPIO.OUT)

GPIO.setup(redButton, GPIO.IN)
GPIO.setup(greenButton, GPIO.IN)
GPIO.setup(blueButton, GPIO.IN)

try:
        while True:
                redButtState = GPIO.input(redButton)
                greenButtState = GPIO.input(greenButton)
                blueButtState = GPIO.input(blueButton)
                if redButtState != oldRedButtState and redButtState == 1:
                        redLEDState = not redLEDState
                        print(f'redButtState = {redButtState}, oldState = {oldRedButtState}')
                GPIO.output(redLED, redLEDState)
                oldRedButtState = redButtState
                if greenButtState != oldGreenButtState and greenButtState == 1:
                        greenLEDState = not greenLEDState
                GPIO.output(greenLED, greenLEDState)
                oldGreenButtState = greenButtState
                if blueButtState != oldBlueButtState and blueButtState == 1:
                        blueLEDState = not blueLEDState
                GPIO.output(blueLED, blueLEDState)
                oldBlueButtState = blueButtState
                time.sleep(.1)
                print(f'redLEDState = {redLEDState} greenLEDState = {greenLEDState}, blueLEDState = {blueLEDState}')
except KeyboardInterrupt:
        GPIO.cleanup()
