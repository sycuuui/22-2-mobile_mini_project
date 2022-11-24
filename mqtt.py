#publisher

import time
import paho.mqtt.client as mqtt
import project

def on_connect(client,userdata,flag,rc):
    client.subscribe("motor",qos=0)

def on_message(client,userdata,msg):
    msg = int(msg.payload)
    print(msg)
    project.controlMotor()

broker_ip = "localhost"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_ip,1883)
client.loop_start()

while (True):
    time.sleep(1)

client.loop_stop()
client.disconnect()
