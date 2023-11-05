'''Imagine I have a tank of water with a sensor in it that reads "full" if the tank is more than half full and "empty" if it's less than half full. Problem is, the tank is in a very noisy industrial environment - things bang into the tank and the water sloshing around in the tank tends to trigger the sensor even when I don't want it to.

So, I run a tiny hose into the tank that pumps a trickle of water into it. If nobody is actively trying to fill or drain the tank, the trickle will eventually fill the tank completely and my sensor will always read "full" instead of triggering randomly if the tank gets bumped. Conversely, I could drill a tiny hole and let the tank leak until it was empty so the tank would always eventually go to "empty" if nobody's filling or draining it.

Pull-up (tiny hose) and pull down (tiny hole) resistors do something roughly similar for wires in a circuit. A wire that's not connected to anything or (and this is the important part) connected only to devices (like an input pin on a microcontroller) that aren't actively driving it is like the half-full tank of water - the electrons in the wire get sloshed around by being bumped by stray electrical or magnetic fields in the circuit and cause the input pins to read erratic values or malfunction entirely.

By pulling up or pulling down a wire in a circuit we stabilize it so that it will always settle at a known voltage whether the chips it's connected to are powered or not. In doing so we help prevent our circuit from failing in weird and erratic ways.'''

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
inPin = 40

GPIO.setup(inPin,GPIO.IN)

try:
    while True:
        #  need to reset readVal on each iteration so it prints new value.
        readVal = GPIO.input(inPin)
        print(readVal)
        sleep(.25)
except KeyboardInterrupt:
    GPIO.cleanup()