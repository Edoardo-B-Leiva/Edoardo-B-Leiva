__author__ = "Edoardo Borgia Leiva"
__license__ = "GPLv3" # https://www.fsf.org/

##Libraries
from machine import Pin, PWM #Pin usage
from time import sleep #Use of sleep to create intervals
import random as rand
import _thread

##LEDs
statusLed = Pin(25, Pin.OUT) #Status Led (Onboard Pin 25)
led1 = Pin(16, Pin.OUT) #Springfield
led2 = PWM(Pin(17)) #Nuclear
led3 = Pin(18, Pin.OUT) #Tunnels
led4 = Pin(19, Pin.OUT) #Houses & Football Pitch
led5 = PWM(Pin(20)) #Broken FootBall Pitch

##Buttons (Switches)
btn1 = Pin(0, Pin.IN) #Springfield
btn2 = Pin(1, Pin.IN) #Nuclear
btn3 = Pin(2, Pin.IN) #Houses
btn4 = Pin(3, Pin.IN) #Tunnels

##Stop Button
stopBtn = Pin(4, Pin.IN)

##FREQz
led2.freq(1000)

#Code

def main():
    print('ok')
    
def Nuclear():
    while True:
        for duty in range(65025):
            led2.duty_u16(duty)
            sleep(0.0001)
        for duty in range(65025, 0, -1):
            led2.duty_u16(duty)
            sleep(0.0001)

_thread.start_new_thread(Nuclear, ())

#Script Starts HERE!
print('Script Started...')
statusLed.on() ## Indicates that the script is running without any problem.
main()
#END
