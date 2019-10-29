import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BOARD)
rele = 11

GPIO.setup (rele,GPIO.OUT)

while(1):
	GPIO.output(rele,1)
	time.sleep(0.5)
	GPIO.output(rele,0)
	time.sleep(0.5)
