import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def abs():
    a_1=0
    for i in range(7, -1, -1):
        a=1
        for j in range(i):
            a = a*2
        a_1=a_1+a
        number = decimal2binary(a_1)
        GPIO.output(dac, number)
        time.sleep(0.005)
        if GPIO.input(comp)==0:
            a_1=a_1-a
    return a_1

def u_troyka(value):
    return 3.3*n/256

# Выходы
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

#Их настройка
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

spisok_u = []
t = []
t0 = 0

try:
    GPIO.output(troyka, 1)
    t0 = time.time()
    while True:
        n = abs()
        spisok_u.append(u_troyka(n))
        GPIO.output(leds, decimal2binary(n))
        if n>248:
            GPIO.output(troyka, 0)
            break
    while True:
        n = abs()
        spisok_u.append(u_troyka(n))
        GPIO.output(leds, decimal2binary(n))
        if n<2:
            break
    t1 = time.time()

    period_iz = t1 - t0
    for i in range(len(spisok_u)):
        t.append(i*period_iz/len(spisok_u))
    plt.plot(t,spisok_u)

    with open("data.txt", "w") as outfile:
        outfile.write("\n".join([str(item) for item in spisok_u]))
    with open("settings.txt", "w") as outfile:
        outfile.write("\n".join([str(len(spisok_u)/period_iz), str(3.3/256)]))
    print (period_iz, period_iz/len(spisok_u), len(spisok_u)/period_iz, 3.3/256)

    plt.show()
except ValueError:
    print("Не а")
finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()