import RPi.GPIO as GPIO

GPIO_PWM = 22
FREQUENCY = 100
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PWM, GPIO.OUT)
pwmOut = GPIO.PWM(GPIO_PWM, FREQUENCY)
pwmOut.start(0)
try:
    while True:
        myDutyCycle = int(input())
        pwmOut.ChangeDutyCycle(myDutyCycle)
finally:
    GPIO.cleanup()