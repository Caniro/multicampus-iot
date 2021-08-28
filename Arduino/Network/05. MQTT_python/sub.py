# MQTT 사용
import paho.mqtt.client as mqtt

def on_connect (client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    if rc == 0:
        client.subscribe("iot/#")
    else:
        print("연결 실패 : ", rc)

# binary배열.decode() : binary를 문자열로 변환
# 문자열.encode() : 문자열을 binary로 변환
def on_message(client, userdata, msg):
    value = float(msg.payload.decode())
    print(f"{msg.topic} {value}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect("localhost")
    client.loop_forever()

except Exception as e:
    print("에러 :", e)
