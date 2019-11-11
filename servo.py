# imports
import RPi.GPIO as GPIO
import time

# fio branco: 5 V
# fio preto: GND
# fio cinza: porta 18
# abertura a 47°(fechado) a 80º(aberto)

# define o pino(BCM) para o servo
servo_pin = 18

#Ajuste estes valores para obter o intervalo completo do movimento do servo
deg_0_pulse   = 0.5 
deg_180_pulse = 2.5
f = 100.0

# Faca alguns calculos dos parametros da largura do pulso
period = 1000/f
k      = 100/period
deg_0_duty = deg_0_pulse*k
pulse_range = deg_180_pulse - deg_0_pulse
duty_range = pulse_range * k

#Iniciar o pino gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)
pwm = GPIO.PWM(servo_pin,f)
pwm.start(0)

# calcula o ângulo a ser passado para o servo
def set_angle(angle):
        duty = deg_0_duty + (angle/180.0)* duty_range
        pwm.ChangeDutyCycle(round(duty,4))
        print(round(duty,4))

# roda o loop
ang = 0
try:
        while True:
                angle = input ("Enter angle (0 a 180): ")
                set_angle(int(angle))

# fecha os GPIO
finally:
        print("cleaning up")
        GPIO.cleanup()
