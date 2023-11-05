
from time import sleep
import RPi.GPIO as GPIO

delay = .1
inPin = 40
outPin = 38


GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:

        readVal = GPIO.input(inPin)
        print(readVal)

        if readVal == 1:
            GPIO.output(outPin, 0)
        if readVal == 0:
            GPIO.output(outPin, 1)

        # if GPIO.input(inPin) == GPIO.LOW:
        #     GPIO.output(outPin, GPIO.HIGH)
        #     print("Button Pressed")
        # else:
        #     GPIO.output(outPin, GPIO.LOW)
        #     print("Button Not Pressed")
        # sleep(delay)
    
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Goodbye")
