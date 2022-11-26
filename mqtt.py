#publisher

import time
import paho.mqtt.client as mqtt
import button
import motor
from datetime import datetime

def on_connect(client,userdata,flag,rc):
    client.subscribe("motor",qos=0) #topic=motor

def on_message(client,userdata,msg):
    msg = int(msg.payload)
    print(msg)
    motor.controlMotor(msg)

broker_ip = "localhost"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_ip,1883)
client.loop_start()

while (True):
    isBtn = button.driver()
    if(isBtn==1):
         now=datetime.now()
         nowTime=now.strftime('%Y-%m-%d %H:%M:%S')
         client.publish("driver",nowTime,qos=0)
    time.sleep(1)


client.loop_stop()
client.disconnect()
