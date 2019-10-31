import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers

pin = 7

GPIO.setup(pin,GPIO.OUT)

try:
    while 1:
        GPIO.output(pin,0) 
        print ("Baixo")
        time.sleep(0.5)
        GPIO.output(pin,1)
        print ("Alto")
        time.sleep(0.5)
		
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()

