#Define Libraries
import RPi.GPIO as gpio
import time

#Configuring don’t show warnings 
gpio.setwarnings(False)

#Configuring GPIO
gpio.setmode(gpio.BCM)
gpio.setup(17,gpio.OUT)
gpio.setup(24,gpio.OUT)
gpio.setup(27,gpio.OUT)

#Configure the pwm objects and initialize its value
pwmBlue = gpio.PWM(24,120)
pwmBlue.start(0)

pwmRed = gpio.PWM(17,120)
pwmRed.start(0)

pwmGreen = gpio.PWM(27,120)
pwmGreen.start(0)
 
#Create the dutycycle variables
dcBlue = 0
dcRed  = 0
dcGreen = 0

passo = 5
vel = 0.05
#Loop infinite
while True:
   
    while dcRed < 100:
        dcRed = dcRed + passo
        pwmRed.ChangeDutyCycle(dcRed)
        time.sleep(vel)
        
    while dcRed > 0:
        dcRed = dcRed - passo
        pwmRed.ChangeDutyCycle(dcRed)
        time.sleep(vel)
        
    while dcBlue < 100:
        dcBlue = dcBlue + passo
        pwmBlue.ChangeDutyCycle(dcBlue)
        time.sleep(vel)
        
    while dcBlue > 0:
        dcBlue = dcBlue - passo
        pwmBlue.ChangeDutyCycle(dcBlue)
        time.sleep(vel)
        
    while dcGreen < 100:
        dcGreen = dcGreen + passo
        pwmGreen.ChangeDutyCycle(dcGreen)
        time.sleep(vel)
        
    while dcGreen > 0:
        dcGreen = dcGreen - passo
        pwmGreen.ChangeDutyCycle(dcGreen)
        time.sleep(vel)

#End code
gpio.cleanup()
exit()

