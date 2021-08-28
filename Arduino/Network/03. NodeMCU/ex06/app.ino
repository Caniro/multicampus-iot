/*
    <아두이노>
    ArduinoJson 라이브러리 사용
    - 직렬화(Serializing) : 데이터를 전송할 때 사용
*/

#include <ArduinoJson.h>

void setup()
{
    Serial.begin(115200);

    StaticJsonDocument<256> doc;

    doc["value"] = 42;
    doc["lat"] = 48.748010;
    doc["lon"] = 2.293491;

    // doc.add(1);
    // doc.add(2);

    char output[256];
    serializeJson(doc, output);
    Serial.println(output);
}

void loop() {}
