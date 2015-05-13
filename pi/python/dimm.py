import sys
import RPi.GPIO as GPIO
import time

def dimm(times, pin, freq, p):
    p.start(0)
    for i in range(0,times):
        for dc in range(1,100):
           p.ChangeDutyCycle(dc)
           time.sleep(0.02)
        time.sleep(0.5)
        for dc in range(100,1,-1):
           p.ChangeDutyCycle(dc)
           time.sleep(0.02)
        time.sleep(0.5)

GPIO.setmode(GPIO.BCM)

times = int(sys.argv[1])
pin = int(sys.argv[2])
freq = int(sys.argv[3])
#on = 1
#off = 1
#if(len(sys.argv) > 3):
#    on = float(sys.argv[3])
#if(len(sys.argv) > 4):
#    off = float(sys.argv[4])

GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, freq)

dimm(times, pin, freq, p)

p.stop();

GPIO.cleanup()
