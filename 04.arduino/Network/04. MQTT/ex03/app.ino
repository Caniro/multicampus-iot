/*
    NodeMCU MQTT
    DHT11, cds 센서 사용
*/

#include <MqttCom.h>
#include <DHT.h>
#include <Analog.h>

const char *ssid = "HanGuest1";
const char *password = "00001234";
const char *mqtt_server = "192.168.117.20";

MqttCom com;
DHT dht11(D6, DHT11);
Analog cds(A0, 0, 100);

int value = 0;

void publish()
{
    char msg[50];
    float fh = dht11.readHumidity();
    float fc = dht11.readTemperature();
    int illu = cds.read();

    if (isnan(fh) || isnan(fc))
    {
        Serial.println("DHT11 read failed");
        return ;
    }

    com.publish("iot/hong/bedroom/temp", fc);
    com.publish("iot/hong/bedroom/humi", fh);
    com.publish("iot/hong/bedroom/illu", illu);
}

void setup()
{
    com.init(ssid, password);
    com.setServer(mqtt_server);
    com.setInterval(2000, publish);
    dht11.begin();
}

void loop()
{
    com.run();
}
