from machine import Pin
from networking import wifi, socketServer

def app():
    GPIO0 = 5
    pinLED = Pin(GPIO0, Pin.OUT)
    pinLED.low()
    # connecteren met netwerk
    wifi.connectWIFI()
    if socketServer.start() == False:
        wifi.disconnectWIFI()
        return 0
        
    while True:
        status = socketServer.waitCn()
        if status < 0:
            print("Wrong command")
        elif status == 0:
            print("Halt ESP")
            break
        else:
            socketServer.sendData("OK")
            res = socketServer.readData()
            pinLED.value(int(res))
            socketServer.sendData("OK")
            socketServer.stopClient()

    pinLED.low()
    wifi.disconnectWIFI()
    
app()
