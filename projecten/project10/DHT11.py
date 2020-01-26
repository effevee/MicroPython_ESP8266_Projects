from machine import Pin
import dht
import time
import utime

# datapin van DHT11 zit op pin D4 (GPIO2)
DataPin = 2

# initialisatie DHT11 sensor
sensor = dht.DHT11(Pin(DataPin))

while True:
    # lees sensorwaarde
    sensor.measure()
    # lees tijd (geen RTC !)
    tijd = utime.localtime()
    # toon waarde
    print("{:2d}/{:2d}/{:4d} {:2d}:{:2d}:{:2d} - {:.1f}C - {:.1f}%".format(tijd[2], tijd[1], tijd[0], tijd[3], tijd[4], tijd[5], sensor.temperature(), sensor.humidity()))
    # wacht 10 sec
    time.sleep(10)