import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

inputPin1 = 40
inputPin2 = 38
pwmPin = 37
input1state = 0
prevInput1state = 0
prevInput2state = 0
input2state = 0
dutyCycle = 0
inputEventExponent = 0

GPIO.setup(pwmPin,GPIO.OUT)
GPIO.setup(inputPin1, GPIO.IN)
GPIO.setup(inputPin2, GPIO.IN)
myPWM = GPIO.PWM(pwmPin,100)
myPWM.start(0)
myPWM.ChangeFrequency(60)
print(f'dutyCycle:{dutyCycle}')
print(f"input1state:{input1state}")
try:
        while True:
                input1state = GPIO.input(inputPin1)
                input2state = GPIO.input(inputPin2)
                if input1state != prevInput1state and input1state == 1:
                        inputEventExponent += 1
                        dutyCycle = (1.5849) ** inputEventExponent
                        if dutyCycle > 100.0:
                                inputEventExponent = 10
                                dutyCycle = 100.0
                print(f'Increased Duty cycle % changed to : {dutyCycle}')
                prevInput1state = input1state
                if input2state != prevInput2state and input2state == 1:
                        inputEventExponent -= 1
                        dutyCycle = (1.5849) ** inputEventExponent
                        if dutyCycle < 1.0:
                                inputEventExponent = 0
                                dutyCycle = 0.0
                myPWM.ChangeDutyCycle(dutyCycle)
                print(f'Decreased Duty Cycle % changed to: {dutyCycle}')
                prevInput2state = input2state
                sleep(.1)
except KeyboardInterrupt:
        myPWM.stop()
        GPIO.cleanup()
