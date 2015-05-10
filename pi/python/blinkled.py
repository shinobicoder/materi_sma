import sys
import RPi.GPIO as GPIO
import time

def blink(times, pin, on, off):
    for i in range(0,times):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(on)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(off)

GPIO.setmode(GPIO.BCM)


times = int(sys.argv[1])
pin = int(sys.argv[2])
on = 1
off = 1
if(len(sys.argv) > 3):
    on = float(sys.argv[3])
if(len(sys.argv) > 4):
    off = float(sys.argv[4])

GPIO.setup(pin, GPIO.OUT)
blink(times, pin, on, off)

GPIO.cleanup()
