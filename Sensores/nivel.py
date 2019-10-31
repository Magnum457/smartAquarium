# imports
import RPi.GPIO as GPIO
import time

# configurando os GPIO
def setup():
    GPIO.setmode (GPIO.BCM) # usa o mapa de portas da placa
    bot = 13
    GPIO.setup (bot, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
    estado = 0
    return bot, estado

def loop_nivel():
    try:    
        while True:
            bot, estado = setup()
            if GPIO.input(bot)==0:
                    estado = 0
                    print "Ligado"

            elif GPIO.input(bot)==1:
                    estado = 1
                    print "Desligado"
            time.sleep(1)
                        
    finally:
        print("fechando as GPIOs")
        GPIO.cleanup()

