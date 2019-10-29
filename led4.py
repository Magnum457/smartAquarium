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
pwmBlue = gpio.PWM(24,100)
pwmBlue.start(0)

pwmRed = gpio.PWM(17,100)
pwmRed.start(0)

pwmGreen = gpio.PWM(27,100)
pwmGreen.start(0)
 
#Create the dutycycle variables
dcBlue = 0
dcRed  = 0
dcGreen = 0
vel = 1

state = 'down'
#Loop infinite
while True:
    if state == 'down':
        vel = vel/1.2
    else:
        vel = vel*1.2
        
    if vel <= 0.05:
        state = 'up'
    
    if vel > 1:
        state = 'down'
        
    print(state)
    print(vel)
    #increment gradually the luminosity
    pwmBlue.ChangeDutyCycle(100)
    time.sleep(vel)
    pwmBlue.ChangeDutyCycle(0)
    time.sleep(vel)
    
    pwmRed.ChangeDutyCycle(100)
    time.sleep(vel)
    pwmRed.ChangeDutyCycle(0)
    time.sleep(vel)
    
    pwmGreen.ChangeDutyCycle(100)
    time.sleep(vel)
    pwmGreen.ChangeDutyCycle(0)
    time.sleep(vel)

#End code
gpio.cleanup()
exit()