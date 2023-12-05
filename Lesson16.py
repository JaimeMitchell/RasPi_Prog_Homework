import RPi.GPIO as GPIO
import ADC0834
import time

GPIO.setmode(GPIO.BCM)
ADC0834.setup()

# set up dimmable LED
pwmPin = 12
GPIO.setup(pwmPin,GPIO.OUT)
LED_PWM = GPIO.PWM(pwmPin,100)
LED_PWM.start(0)
try:
    while True:
        analogVal=ADC0834.getResult(0)
        print(analogVal)
        analogVal/=10.24
        print(analogVal)
        LED_state = LED_PWM.start(analogVal)
        LED_PWM.ChangeDutyCycle(analogVal)
        time.sleep(.1)


except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Pins CLEANED UP!')
