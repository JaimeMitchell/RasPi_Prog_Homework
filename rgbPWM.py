import RPi.GPIO as GPIO
import time
from vpython import *

GPIO.setmode(GPIO.BOARD)

# set to PWM pins
rLED = 37
gLED = 35
bLED = 32

rBut = 40
gBut = 38
bBut = 36

# number of button presses
rPresses_exponent = 0
gPresses_exponent = 0
bPresses_exponent = 0

# duty cycle
rDC = 0
gDC = 0
bDC = 0

# button states
rButState = 0
gButState = 0
bButState = 0

# previous button states
prevRbutState = 0
prevGbutState = 0
prevBbutState = 0

# set up GPIO pins
GPIO.setup(rLED, GPIO.OUT)
GPIO.setup(gLED, GPIO.OUT)
GPIO.setup(bLED, GPIO.OUT)

# set initial duty cycle
GPIO.output(rLED, rDC)
GPIO.output(gLED, gDC)
GPIO.output(bLED, bDC)

# set up PWM pins as PWM objects
# args are pwm pins, frequency set to human eye range
rPWM = GPIO.PWM(rLED, 60)
gPWM = GPIO.PWM(gLED, 60)
bPWM = GPIO.PWM(bLED, 60)      

# start PWM with 0% duty cycle
rPWM.start(0)
gPWM.start(0)
bPWM.start(0)

# set up buttons as inputs
GPIO.setup(rBut, GPIO.IN)
GPIO.setup(gBut, GPIO.IN)
GPIO.setup(bBut, GPIO.IN)

mySphere = sphere(color=color.white, radius=1 , pos=vector(0,2.5,0))
myCylinder = cylinder(color=color.white, radius=1, length=2.5, axis=vector(0,1,0))
myBase = cylinder(color=color.white, radius = 1.2, length = .25, axis=vector(0,1,0))
myLeg1 = box(pos=vector(-.75, -1, 0),size=vector(.1,2,.1), color=vector(.2,.2,.2))
myLeg2 = box(pos=vector(.75, -1, 0),size=vector(.1,2.25,.1), color=vector(.2,.2,.2))
myBreadBoard = box(pos=vector(0, -1.5, 0),size=vector(4,.25,2), color=color.white)

try:
        while True:
                rate(20)
                #0 get button states
                rButState = GPIO.input(rBut)
                gButState = GPIO.input(gBut)
                bButState = GPIO.input(bBut)
               
                #1 if button state has changed from 0 to 1 and is now 1
                if rButState != prevRbutState and rButState == 1:

                        #1.1 button pressed so increases exponent by 1
                        rPresses_exponent += 1

                        #1.2 if more than 10 presses, reset to 0 and continue out of loop.
                        if rPresses_exponent > 10:
                                rPresses_exponent = 0
                                rDC = 0.0
                                
                        else:
                                #1.3 calculate duty cycle
                                rDC = (1.5849) ** rPresses_exponent

                                #1.4 if duty cycle is greater than 100, set to 100
                                if rDC > 100.0:
                                        rDC = 100.0
                print(f'rPresses_exponent: {rPresses_exponent}, rDC: {rDC}')

                #2 change duty cycle
                rPWM.ChangeDutyCycle(rDC)

                #3 keep track of old button state to avoid multiple changes per button press
                prevRbutState = rButState
        
        
                # ------------------------ Repeat logic for green -------------------------

                if gButState != prevGbutState and gButState == 1:
                        
                        gPresses_exponent += 1
                # experiment with 11 instead of > 10 to see if the same logic bugs out for some reason in the RPi library. Works just fine.
                        if gPresses_exponent == 11:
                                gPresses_exponent = 0
                                gDC = 0
                                
                        else:
                                gDC = (1.5849) ** gPresses_exponent

                        if gDC > 100.0:
                                gDC = 100.0
                print(f' gPresses_exponent: {gPresses_exponent}, gDC: {gDC}')

                gPWM.ChangeDutyCycle(gDC)
                prevGbutState = gButState

                # ------------------------ Repeat logic for blue -------------------------
                
                if bButState != prevBbutState and bButState == 1:
                        bPresses_exponent += 1
                        if bPresses_exponent > 10:
                                bPresses_exponent = 0
                                bDC = 0.0
                        else:
                                bDC = (1.5849) ** bPresses_exponent
                        if bDC > 100.0:
                                bDC = 100.0
                print(f' bPresses_exponent: {bPresses_exponent}, bDC: {bDC}')   
                bPWM.ChangeDutyCycle(bDC)
                prevBbutState = bButState

                print(f'rDC = {rDC} gDC = {gDC}, bDC = {bDC}')
                
                #Convert Duty Cycle for PWM in pi to the 0-1 scale in Visual Python's RGB
                mySphere.color = vector(rDC/25,gDC/25,bDC/25)
                myCylinder.color = vector(rDC/25, gDC/25, bDC/25)
                myBase.color= vector(rDC/25, gDC/25, bDC/25)
                time.sleep(.1)

except KeyboardInterrupt:
        GPIO.cleanup()
        print("GPIO Pins are cleaned up!")
