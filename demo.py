import os
import glob
import time
import RPi.GPIO as GPIO
from random import randint


#Configuring don’t show warnings 
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM) # usa o mapa de portas da placa
pin_nivel = 13
GPIO.setup(pin_nivel,GPIO.IN, pull_up_down=GPIO.PUD_UP) # já configura a porta como HIGH automaticamente


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

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
ang = 50

#Iniciar o pino gpio
GPIO.setup(servo_pin,GPIO.OUT)
pwm = GPIO.PWM(servo_pin,f)
pwm.start(0)
 
#Configuring GPIO
GPIO.setup(17,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

#Configure the pwm objects and initialize its value
pwmBlue = GPIO.PWM(24,100)
pwmBlue.start(0)

pwmRed = GPIO.PWM(17,100)
pwmRed.start(0)

pwmGreen = GPIO.PWM(27,100)
pwmGreen.start(0)

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return str(temp_c)
# calcula o ângulo a ser passado para o servo
def set_angle(angle):
        duty = deg_0_duty + (angle/180.0)* duty_range
        pwm.ChangeDutyCycle(round(duty,3))


while True:
    print('Temperatura: ' + read_temp() + 'ºC')
    if (GPIO.input(pin_nivel) == 1):
        print('Abaixo do Nível')
    else:
        print('Acima do Nível')
    ang = ang + 10
    if ang > 80:
        ang = 50
    set_angle(ang)
    
    pwmRed.ChangeDutyCycle(randint(0,100))
    pwmBlue.ChangeDutyCycle(randint(0,100))
    pwmGreen.ChangeDutyCycle(randint(0,100))
    time.sleep(0.1)
    
