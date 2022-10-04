import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
troyka = 17
comp = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
a = int()

def dec2bin(a):
    return [int(i) for i in bin(a)[2:].zfill(8)]
def abc():
    for i in range(256):
        signal = dec2bin(i)
        GPIO.output(dac, signal)
        time.sleep(0.001)
        compvalue=GPIO.input(comp)
        if compvalue==0:
            return i
try:
    while True:
        n = abc()
        voltage = float(int(3.3*n/256*100)/100)
        print(n, "voltage = ", voltage)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()