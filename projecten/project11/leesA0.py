from machine import ADC
import time

# initialisatie analoge poort A0
adc = ADC(0)

while True:
    # toon uitgelezen waarde
    print(adc.read())
    
    # pause
    time.sleep_ms(500)