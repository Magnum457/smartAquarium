# a diferença desse para o outro é porque esse atualiza os angulos em determinado intervalo e não seta eles automaticamente 

# imports
    import RPi.GPIO as GPIO
    import time

# configuração das portas
    servoPIN = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

# configura a porta escolhida como PWM e inicia ela com uma frequencia de 50Hz
    p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
    p.start(2.5) # Initialization

# loop
try:
  while True:
    p.ChangeDutyCycle(12) # atualiza o ciclo passado para a porta que mapea para um angulo no servo, como não tem o calculo não é passado o angulo diretamente
    time.sleep(0.1)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.1)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)
except KeyboardInterrupt:
  p.stop() # fecha a porta
  GPIO.cleanup() # fecha as GPIO
