#Define Libraries
import RPi.GPIO as gpio
import time

#Configuring don’t show warnings 
gpio.setwarnings(False)

#Configuring GPIO
gpio.setmode(gpio.BCM)
gpio.setup(17,gpio.OUT)
gpio.setup(24,gpio.OUT)
gpio.setup(22,gpio.OUT)

#Configure the pwm objects and initialize its value
pwmBlue = gpio.PWM(24,100)
pwmBlue.start(0)

pwmRed = gpio.PWM(17,100)
pwmRed.start(100)

pwmGreen = gpio.PWM(22,100)
pwmGreen.start(100)
 
#Create the dutycycle variables
dcBlue = 0
dcRed  = 100

#Loop infinite
while True:
   
    #increment gradually the luminosity
    pwmBlue.ChangeDutyCycle(dcBlue)
    time.sleep(0.001)
    dcBlue = dcBlue + 1
    if dcBlue == 100:
        dcBlue = 0

    #decrement gradually the luminosity
    pwmRed.ChangeDutyCycle(dcRed)
    time.sleep(0.001)
    dcRed = dcRed - 1
    if dcRed == 0:
        dcRed = 100
    
#End code
gpio.cleanup()
exit()