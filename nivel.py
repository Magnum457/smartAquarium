# imports
import RPi.GPIO as GPIO

# configurando os GPIO
def setup():
    GPIO.setmode (GPIO.BCM) # usa o mapa de portas da placa
    bot = 26
    GPIO.setup (bot,GPIO.IN, pull_up_down=GPIO.PUD_UP) # já configura a porta como HIGH automaticamente
    estado = 0
    return bot, estado

try:
    
    def loop_nivel():
            bot, estado = setup()
            if GPIO.input(bot)==0 and estado == 1:
                    estado = 0
                    return "Ligado"

            elif GPIO.input(bot)==1 and estado == 0:
                    estado = 1
                    return "Desligado"
finally:
    print("fechando as GPIOs")
    GPIO.cleanup()
