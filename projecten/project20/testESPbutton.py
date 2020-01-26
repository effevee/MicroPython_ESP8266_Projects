from machine import Pin
from networking import wifi, socketHTTPRequest
import time

# gpio button met pullup weerstand
ButNum = 14
button = Pin(ButNum, Pin.IN, Pin.PULL_UP)

# connecteren op wifi
wifi.connectWIFI()

while True:
    # knop gedrukt 
    if not button.value():
        # stuur GET request naar button op webserver RPi
        res = socketHTTPRequest.sendGETRequest("/button_2")
        print("button pushed GET request: {}".format(res))
        # even wachten
        time.sleep_ms(300)
        # wachten op knop los
        while not button.value():
            pass
            
# disconnect van wifi
wifi.disconnectWIFI()