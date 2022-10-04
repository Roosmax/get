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
    signal1=128
    signal2=64
    answer=0
    for i in range(8):
        signal = dec2bin(int(answer))
        GPIO.output(dac, signal)
        time.sleep(0.001)
        compvalue=GPIO.input(comp)
        if(compvalue==0):
            if(answer!=0):
                answer-=signal2
        else:
            answer += signal1
        signal1/=2
        signal2/=2
    return int(answer)
print(abc())

try:
    while True:
        n = abc()
        voltage = float(int(3.3*n/256*100)/100)
        print("ADC value =", n, " -> ", dec2bin(n), "voltage = ", voltage)
finally:
    GPIO.output(dac, 1)
    GPIO.cleanup()