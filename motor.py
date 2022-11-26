import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#모터
moter = 18 #moter GPIO18에 연결
GPIO.setup(moter,GPIO.OUT)
pwm = GPIO.PWM(moter,50)
pwm.start(3.0)

def controlMotor(angle):
        pwm.ChangeDutyCycle(angle)
