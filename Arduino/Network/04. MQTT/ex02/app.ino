/*
    NodeMCU MQTT
    MqttCom 클래스화
*/

#include <MqttCom.h>
#include <Led.h>

const char *ssid = "HanGuest1";
const char *password = "00001234";
const char *mqtt_server = "192.168.117.6";

MqttCom com;

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

void publish()
{
    char msg[50];
    ++value;
    sprintf(msg, "hello world #%ld", value);
    Serial.print("Publish message: ");
    Serial.println(msg);
    com.publish("outTopic", msg);
}

void setup()
{
    com.init(ssid, password);
    com.setServer(mqtt_server, "inTopic", callback);
    com.setInterval(2000, publish);
}

void loop()
{
    com.run();
}
