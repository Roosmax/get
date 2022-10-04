import RPi.GPIO as GPIO

def decimal2binary(a):
    return [int(i) for i in bin(a)[2:].zfill(8)]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
try:
    while True:
        n = input()
        if n.isdigit():
            n = int(n)
            if 0 <= n and n <= 255:
                GPIO.output(dac[n], decimal2binary[n])
                print("Предполагаемое напряжение", round((3.3/256 * n, 2), "B")
            elif n < 0:
                print("Меньше нуля")
            else:
                print("Ошибка")
        else:
            if a == q:
                break
            print("Ошибка")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()