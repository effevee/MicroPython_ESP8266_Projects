from machine import Pin, PWM
import time

# externe LED zit op pin D1 (GPIO5)
PinNum = 5

# pwm initialisatie
pwm1 = PWM(Pin(PinNum))
pwm1.freq(60)
pwm1.duty(0)

step = 100
for i in range(10):
    # oplichten
    while step < 1000:
        pwm1.duty(step)
        time.sleep_ms(500)
        step+=100
    # uitdoven    
    while step > 0:
        pwm1.duty(step)
        time.sleep_ms(500)
        step-=200

# pwm resetten        
pwm1.deinit()