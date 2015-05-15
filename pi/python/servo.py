import sys
import RPi.GPIO as GPIO
import time

def position(angle, pin, freq, pwm):
    # hitung lebar sinyal yang diperlukan
    outPulseWidth = (angle+45)/90
    # hitung panjang gelombang satu siklus sinyal
    waveLength = 1000/freq
    # hitung persentasi sinyal aktif (HIGH)
    dutyCycle = (outPulseWidth*100)/waveLength  
    p.start(dutyCycle)
    time.sleep(1)
    
GPIO.setmode(GPIO.BCM)

angle = float(sys.argv[1])
pin = int(sys.argv[2])
freq = int(sys.argv[3])

GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, freq)

position(angle, pin, freq, p)

p.stop();

GPIO.cleanup()
