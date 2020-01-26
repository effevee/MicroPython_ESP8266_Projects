from machine import Pin
import time

# externe LED zit op pin D1 (GPIO5)
PinNum = 5
# button zit op pin D5 (GPIO14)
ButNum = 14

led = Pin(PinNum, Pin.OUT)
# we gebruiken de ingebouwde pullup weerstand
button = Pin(ButNum, Pin.IN, Pin.PULL_UP)

while True:
    if not button.value():
        # toggle funktie
        led.value(not led.value())
        time.sleep_ms(300)
        while not button.value():
            pass
            