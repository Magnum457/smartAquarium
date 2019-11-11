import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM) # usa o mapa de portas da placa
bot = 6
GPIO.setup (bot, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
estado = 0

while True:
    if GPIO.input(bot)==0:
            estado = 0
            print("Ligado")

    elif GPIO.input(bot)==1:
            estado = 1
            print("Desligado")
    time.sleep(1)