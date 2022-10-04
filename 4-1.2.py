import RPi.GPIO as GPIO

def decimal2binary(a):
    return [int(i) for i in bin(a)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 0, 0, 0, 0, 0, 0, 0]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
try:
    while True:
        n = input()
        if n == 'q':
            break
        n = float(n)
        if n - int(n) != 0:
            print("Дробное")
            break
        n = int(n)
        if n < 0:
            print("Меньше нуля")
            break
        if n > 255:
            print("Превышает допустимые значения")
            break
        number = decimal2binary(n)
        for a in range(8):
            GPIO.output(dac[a], number[a])
        print("Предполагаемое напряжение", round((3.3)/256 * n, 2), "B")
except ValueError:
    if type(n) == str:
        print("Не является числом")
finally:
    for a in range(8):
        GPIO.output(dac[a], 0)
    GPIO.cleanup()