import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 초음파
trig=20
echo=16
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)
def measureDistance(trig, echo):
        time.sleep(0.5)
        GPIO.output(trig, True) 
        GPIO.output(trig, False) # 신호가 1-> 0으로 떨어질 때 초음파발생
        while(GPIO.input(echo) == 0):
                pass
        pulse_start = time.time()
        while(GPIO.input(echo) == 1):
                pass
        pulse_end = time.time() 
        pulse_duration = pulse_end - pulse_start
        return 340*100/2*pulse_duration

#LED
led = 6 #초록색
error = 5 #빨간색 3번 연속으로 비밀번호 잘못 입력하면 반짝
empty = 13
GPIO.setup(led,GPIO.OUT)
GPIO.setup(error,GPIO.OUT)
GPIO.setup(empty,GPIO.OUT)
ledOn=1
ledOff=0
def ledOnOff(led,onOff):
        GPIO.output(led,onOff)

#스위치
button1 = 21 #라즈베리쪽에 있는 것
button2 = 12
button3 = 25
button4 = 23
GPIO.setup(button1,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(button2,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(button3,GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(button4,GPIO.IN,GPIO.PUD_DOWN)
pwdArray=[] #비밀번호 입력받는 배열

def changeStr(array): # 배열을 문자열로 바꿔줌
        pwd = ''.join(map(str,array))
        return pwd

errorCount = 0 #비밀번호를 잘못 입력 했을 때 count
userPwd = 1212 #사용자의 비밀번호

#모터
moter = 18 #moter GPIO18에 연결
GPIO.setup(moter,GPIO.OUT)
pwm = GPIO.PWM(moter,50)
pwm.start(3.0)

def controlMotor():
        pwm.ChangeDutyCycle(7.5)

while True :
        distance = measureDistance(trig, echo)
        pwm.ChangeDutyCycle(3.0) #0도로 설정
        if(distance<=5):
                print("택배상자가 들어왔습니다")
                ledOnOff(led,ledOn)
                ledOnOff(empty,ledOff)
        else:
                ledOnOff(led,ledOff)
                ledOnOff(empty,ledOn)
        #조도 센서가 어두우면 pwm.ChangeDutyCycle(3.0)으로 하기 위에꺼 없애고
        btnStatus1 = GPIO.input(button1)
        btnStatus2 = GPIO.input(button2)
        btnStatus3 = GPIO.input(button3)
        btnStatus4 = GPIO.input(button4)
        if(btnStatus1==1): #1번 스위치를 누르면 배열에 1추가
                pwdArray.append(1)
                print(1)
        elif(btnStatus2==1): #2번 스위치를 누르면 배열에 2추가
                pwdArray.append(2)
                print(2)
        elif(btnStatus3==1): #3번 스위치를 누르면 배열에 3추가
                pwdArray.append(3)
                print(3)
        elif(btnStatus4==1):
                pwdArray.append(4)
                print(4)       
        if(len(pwdArray) == 4): #배열의 길이가 4일때
                pwd=changeStr(pwdArray) #배열을 비교하기 위해서 문자열로 바꿈
                if(str(userPwd)!=pwd): #사용자의 비밀번호와 입력받은 비밀번호가 다른 경우
                        print(pwdArray)
                        print(changeStr(pwdArray))
                        pwdArray.clear() #배열 초기화
                        errorCount = errorCount +1 
                        print("다시 입력하세요") 
                else: #사용자의 비밀번호와 입력받은 비밀번호가 같으면 무한루트 탈출
                        pwm.ChangeDutyCycle(7.5) #비밀번호가 맞으t면 90도로 설정
                        time.sleep(1.0)
                        print(pwdArray)
                        print(changeStr(pwdArray))
                        ledOnOff(error,ledOff)
                if(errorCount%3==0): #errorCount가 3번 연속으로 틀린다면 노란색 LED켜짐(비밀번호를 제대로 입력 받을 때까지 켜놓음)
                                ledOnOff(error,ledOn)

