import time
import RPi.GPIO as GPIO
#from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button4 = 23
GPIO.setup(button4,GPIO.IN,GPIO.PUD_DOWN)
def driver():
        global button4
        btnStatus4 = GPIO.input(button4)
        if(btnStatus4==1):
                print("택배 요청")
                #now=datetime.now()
                #return now.strftime('%Y-%m-%d %H:%M:%S')
                return 1
