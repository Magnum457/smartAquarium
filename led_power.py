import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM) # usa o mapa de portas da placa
pin_pw = 12
GPIO.setup (pin_pw, GPIO.OUT)
pin_con = 5
GPIO.setup (pin_con, GPIO.OUT) 

for i in range(10):
        GPIO.output(pin_pw,0)
        GPIO.output(pin_con,1)
        time.sleep(0.5)
        GPIO.output(pin_pw,1)
        GPIO.output(pin_con,0)
        time.sleep(0.5)
    
#End code
GPIO.cleanup()
exit()