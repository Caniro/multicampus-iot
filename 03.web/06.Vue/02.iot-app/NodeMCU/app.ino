#include <MqttCom.h>
#include <DHT.h>
#include <Analog.h>
#include <Led.h>
#include <ArduinoJson.h>

const char *ssid = "HanGuest1";
const char *password = "00001234";
const char *mqtt_server = "192.168.117.20";

MqttCom com;
DHT dht11(D6, DHT11);
Analog cds(A0, 100, 0);
// D1, D2는 MiniCom의 I2C 통신때문에 사용 못하는 듯
Led livingroom_led(D5);
Led kitchen_led(D7);
Led bedroom_led(D8);

const int doc_size = 512;

StaticJsonDocument<doc_size> Deserialize(const String& str)
{
    StaticJsonDocument<doc_size> doc;

    auto error = deserializeJson(doc, String(str));
    if (error)
    {
        Serial.print("deserializeJson() failed with code");
        Serial.println(error.c_str());
    }
    return doc;
}

void ControlLed(const String& place, const String& value)
{
    if (place == "livingroom")
        value == "on" ? livingroom_led.on() : livingroom_led.off();
    else if (place == "kitchen")
        value == "on" ? kitchen_led.on() : kitchen_led.off();
    else if (place == "bedroom")
        value == "on" ? bedroom_led.on() : bedroom_led.off();
}

void Callback(char *topic, byte *payload, unsigned int length)
{
    char buf[doc_size];
    memcpy(buf, payload, length);
    buf[length] = '\0';

    auto doc = Deserialize(buf);
    String place = doc["place"];
    String value = doc["value"];
    ControlLed(place, value);
}

void Publish()
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

    com.publish("iot/hong/sensors/bedroom/temp", fc);
    com.publish("iot/hong/sensors/bedroom/humi", fh);
    com.publish("iot/hong/sensors/bedroom/illu", illu);
}

void setup()
{
    com.init(ssid, password);
    com.setServer(mqtt_server, "iot/hong/control", Callback);
    com.setInterval(2000, Publish);
    dht11.begin();
}

void loop()
{
    com.run();
}
