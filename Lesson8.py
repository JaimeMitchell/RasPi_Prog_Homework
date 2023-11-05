import RPi.GPIO as GPIO
from time import sleep

delay = .1
inPin = 40
outPin = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(outPin, GPIO.LOW)
oldButtonState = 1
try:
    while True:
        buttonState = GPIO.input(inPin)
        print(f"readVal: {buttonState}")

        LEDstate = GPIO.input(outPin)
        print(f"LEDstate: {LEDstate}")

        if buttonState == 1 and oldButtonState == 0:
            LEDstate = not LEDstate 
            GPIO.output(outPin, LEDstate)
        oldButtonState = buttonState
        sleep(delay)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Goodbye") 
