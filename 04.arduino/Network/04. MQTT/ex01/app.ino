/*
    NodeMCU MQTT
*/

#include <WifiMiniCom.h>
#include <PubSubClient.h>
#include <Led.h>

const char *ssid = "HanGuest1";
const char *password = "00001234";
const char *mqtt_server = "192.168.117.6";

WifiMiniCom com;

WiFiClient espClient;
PubSubClient client(espClient);
Led led(BUILTIN_LED);

int value = 0;

void callback(char *topic, byte *payload, unsigned int length)
{
    char buf[128];
    memcpy(buf, payload, length);
    buf[length] = '\0';

    Serial.print("Message arrived [");
    Serial.print(topic);
    Serial.print("] ");
    Serial.println(buf);

    if (buf[0] == '1')
        led.setValue(LOW);
    else
        led.setValue(HIGH);
    com.print(0, topic);
    com.print(1, buf);
}

void reconnect()
{
    while (!client.connected())
    {
        Serial.print("Attempting MQTT connection...");
        if (client.connect("ESP8266Client"))
        {
            Serial.println("connected");
            client.publish("outTopic", "hello world");
            client.subscribe("inTopic");
        }
        else
        {
            Serial.print("failed, rc=");
            Serial.print(client.state());
            Serial.println(" try again in 5 seconds");
            delay(5000);
        }
    }
}

void publish()
{
    char msg[50];
    ++value;
    sprintf(msg, "hello world #%ld", value);
    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish("outTopic", msg);
}

void setup()
{
    com.init(ssid, password);
    com.setInterval(2000, publish);
    client.setServer(mqtt_server, 1883);
    client.setCallback(callback); // 토픽 수신 시 호출할 함수
}

void loop()
{
    com.run();
    if (!client.connected())
        reconnect();
    client.loop();
}
