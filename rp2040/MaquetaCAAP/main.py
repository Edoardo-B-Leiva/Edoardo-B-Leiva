#!/usr/bin/python3

__author__ = "Edoardo Borgia Leiva"
__license__ = "GPLv3" # https://www.fsf.org/
__version__ = "1.0.1"

##Libraries
from machine import Pin, PWM #Pin usage
from time import sleep #Use of sleep to create intervals
import random as rand #Random integers for random sleep time
import _thread #Number of threads, cores and its usage

##LEDs
statusLed = Pin(25, Pin.OUT) #Status Led (Onboard Pin 25)
led1 = Pin(16, Pin.OUT) #Springfield
led2 = PWM(Pin(17)) #Nuclear
led3 = Pin(18, Pin.OUT) #Tunnels
led4 = Pin(19, Pin.OUT) #Houses & Football Pitch
led5 = Pin(20, Pin.OUT) #Broken FootBall Pitch

##Buttons (Switches)
btn1 = Pin(0, Pin.IN) #Springfield
btn2 = Pin(1, Pin.IN) #Nuclear
btn3 = Pin(2, Pin.IN)

##Stop Button
stopBtn = Pin(4, Pin.IN)

##FREQz
led2.freq(1000)

#Env Variables
i = False
j = False

#Code
def main():
    while True:
        FootBallBrokenLight()
        if btn1.value() == 1:
            print('ok2')
            led1.toggle()
            led3.toggle()
            led4.toggle()
            sleep(0.8)
            if i != True:
                i = True
            else:
                i = False
        if btn2.value() == 1:
            print('ok1')
            if j != True:
                j = True
            else:
                j = False
        print('ok')
    
def Nuclear():
     while i == True:
        for duty in range(65025):
            led2.duty_u16(duty)
            sleep(0.0001)
        for duty in range(65025, 0, -1):
            led2.duty_u16(duty)
            sleep(0.0001)
        if btn3.value() == 1:
            continue
     print('Nuclear() stopped.')
        
def FootBallBrokenLight():
    while j == True:
        sleep(rand())
        led5.toggle()
        if btn2.value() == 1:
            continue

_thread.start_new_thread(Nuclear, ()) ##Starts the Nuclear() func into another thread

#Script Start
print('Script Started...')
statusLed.on() ## Indicates that the script is running without any problem.
main()
print('Script Stopped!')
#END
