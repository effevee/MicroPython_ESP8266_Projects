from machine import Pin
import time

# interne LED zit op pin D4 (GPIO2)
PinNum = 2

pin1 = Pin(PinNum, Pin.OUT)

for t in range(10):
    pin1.high()
    time.sleep(1)
    pin1.low()
    time.sleep(1)
    
pin1.high()