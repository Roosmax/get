import RPi.GPIO as GPIO

def decimal2binary(a):
    return [int(i) for i in bin(a)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
p = GPIO.PWM(24, 0.5)
p.start(2)
input(' ')
p.stop(2)
GPIO.cleanup()