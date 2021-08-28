/*
    <아두이노>
    ArduinoJson 라이브러리 사용
    - 역직렬화(Deserializing)
*/

#include <ArduinoJson.h>

void setup()
{
    Serial.begin(115200);

    String buf = "{\"sensor\": \"temp\", \"value\": 20.5}";

    StaticJsonDocument<256> doc;

    auto error = deserializeJson(doc, buf);
    if (error) {
        Serial.print("deserializeJson() failed with code ");
        Serial.println(error.c_str());
        return;
    }
    
    const char* sensor = doc["sensor"];
    float value = doc["value"].as<float>(); // float으로 캐스팅

    Serial.println(sensor);
    Serial.println(value);
}

void loop() {}
