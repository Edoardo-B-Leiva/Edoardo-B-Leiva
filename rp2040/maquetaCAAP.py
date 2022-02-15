__author__ = "Edoardo Borgia Leiva"
__license__ = "GPLv3" # https://www.fsf.org/

##Libraries
from machine import Pin #Pin usage
from time import sleep #Use of sleep to create intervals

##LEDs
statusLed = Pin(25, Pin.OUT) #Status Led (Onboard Pin 25)
led1 = Pin(16, Pin.OUT) #Springfield
led2 = Pin(17, Pin.OUT) #Nuclear
led3 = Pin(18, Pin.OUT) #Tunnels
led4 = Pin(19, Pin.OUT) #Houses & Football Pitch
led5 = Pin(20, Pin.OUT) #Broken FootBall Pitch

##Buttons (Switches)
btn1 = Pin(0, Pin.IN) #Springfield
btn2 = Pin(1, Pin.IN) #Nuclear
btn3 = Pin(2, Pin.IN) #Houses
btn4 = Pin(3, Pin.IN) #Tunnels

##Stop Button
stopBtn = Pin(4, Pin.IN)

#Code

def main():
    while True:
        if led2.value(1):
            led2.off()
        else:
            led2.on()
        sleep(1)
        
    

def stop():
    statusLed.off()
    led2.off()
    
    

    
    
    
print('Script Started...')
statusLed.on() ## Indicates that the script is running without any problem.
main()
stop()
#END
