import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

button = 21
GPIO.setup(button, GPIO.IN)
led = 20
GPIO.setup(led, GPIO.OUT)

delay = .3
button_state = 0
old_button_state = 0
led_state = 0

try:
    while True:
        button_state =  GPIO.input(button)
        print(button_state)
        print(led_state)
        print(old_button_state)
        if button_state != old_button_state:
                if button_state == 1:
                        led_state = not led_state
                        GPIO.output(led, led_state)
        time.sleep(delay)
except KeyboardInterrupt:
    GPIO.cleanup()
