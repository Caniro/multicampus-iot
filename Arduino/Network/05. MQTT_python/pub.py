# MQTT 사용
# publish

import paho.mqtt.client as mqtt

client = mqtt.Client()

try:
    client.connect("localhost")
    client.publish("iot/home2/greet", "Hello World!")
    client.loop(2) # timeout 시간
except Exception as e:
    print("에러 :", e)
