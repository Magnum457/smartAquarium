# imports
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM) # usa o mapa de portas da placa
bot = 23
gpio.setup(bot,gpio.IN, pull_up_down=gpio.PUD_UP) # já configura a porta como HIGH automaticamente
estado = 0

while True:
    print(gpio.input(bot))