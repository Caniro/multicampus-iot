# MQTT 사용
import paho.mqtt.client as mqtt
import sqlite3

con = sqlite3.connect('iot.db')
cursor = con.cursor()

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
    (_, user, place, sensor) = msg.topic.split('/')
    print(f"{user}, {place}, {sensor} : {value}")

    # DB 저장
    sql = f"INSERT INTO sensors (user, place, sensor, value) VALUES ('{user}', '{place}', '{sensor}', '{value}')"
    cursor.execute(sql)
    con.commit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect("localhost")
    client.loop_forever()

except Exception as e:
    print("에러 :", e)
    cursor.close()
    con.close()
