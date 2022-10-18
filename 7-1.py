import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def abc():
    a_1=0
    for i in range(7, -1, -1):
        a=1
        for j in range(i):
            a = a*2
        a_1=a_1+a
        number = dec2bin(a_1)
        GPIO.output(dac, number)
        time.sleep(0.005)
        if GPIO.input(comp)==0:
            a_1=a_1-a
    return a_1

def u_troyka(value):
        return 3.3*n/256

dac = [26,19,13,6,5,11,9,10]
leds=[21,20,16,12,7,8,25,24]
comp = 4
troyka = 17
spisok = []
t = []
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(leds,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT)
GPIO.setup(comp,GPIO.IN)

try:
    GPIO.output(troyka, 1)
    t1 = time.time()
    print("C charging")
    while True:
        n = abc()
        voltage= float(int(3.3*n/256*100)/100)
        spisok.append(u_troyka(n))
        GPIO.output(leds, dec2bin(n))
        if n > 248:
            GPIO.output(troyka, 0)
            break
    print("C uncharging")
    while True:
        n = abc()
        voltage= float(int(3.3*n/256*100)/100)
        spisok.append(u_troyka(n))
        GPIO.output(leds, dec2bin(n))
        if n < 2:
            break
    
    print("Data analyzing")
    t2 = time.time()
    T = t2 - t1
    for i in range(len(spisok)):
        t.append(i*T/len(spisok))
    plt.plot(t, spisok)
    plt.show()

    with open("data.txt", "w") as outfile:
        outfile.write("\n".join([str(item) for item in spisok]))
    with open("data.txt", "w") as outfile:
        outfile.write("\n".join([str(len(spisok)/T)]))
    print(T, T/len(spisok), len(spisok)/T, 3.3/256)
finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()