import paho.mqtt.client as mqtt
from time import sleep
from random import uniform

client = mqtt.Client()

try:
    client.connect("localhost")
    while True:
        client.publish("iot/hong/sensors/livingroom/temp", f'{uniform(0, 100):.2f}')
        client.publish("iot/hong/sensors/livingroom/humi", f'{uniform(0, 100):.2f}')
        client.publish("iot/hong/sensors/livingroom/illu", f'{uniform(0, 100):.2f}')
        client.loop(2)
        sleep(2)
except Exception as err:
    print(f"에러: {err}")
