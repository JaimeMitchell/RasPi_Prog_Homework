import RPi.GPIO as GPIO
import ADC0834
import time
 
GPIO.setmode(GPIO.BCM)
ADC0834.setup()
try:
    while True:
        analogVal=ADC0834.getResult(0)
        print(analogVal)
        time.sleep(.2)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Good to Go')
