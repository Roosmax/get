import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 0, 0, 0, 0, 0, 0, 0]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
try:
    while True:
        n = int(input())
        for a in range(0, 256):
            number = decimal2binary(a)
            for i in range(8):
                GPIO.output(dac[i], number[i])
            time.sleep(n/float(512))
        for a in range(256, -1, -1):
            number = decimal2binary(a)
            for i in range(8):
                GPIO.output(dac[i], number[i])
            time.sleep(n/float(512))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
