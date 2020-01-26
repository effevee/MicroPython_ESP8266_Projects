from machine import Pin
import time

# externe LED zit op pin D1 (GPIO5)
PinNum = 5

pin1 = Pin(PinNum, Pin.OUT)

for t in range(10):
    pin1.low()
    time.sleep(1)
    pin1.high()
    time.sleep(1)
    
pin1.low()