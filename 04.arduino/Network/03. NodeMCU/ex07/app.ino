/*
    OpenWeather OpenAPI 사용
*/

#include <WifiMiniCom.h>
#include <ArduinoJson.h>

const char *ssid = "HanGuest1";
const char *password = "00001234";
WifiMiniCom com;

String host = "api.openweathermap.org";
String url = "http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=c2bf55882617af0dce37b001fcb64dcc&lang=kr&units=metric";

bool request(WiFiClient& client)
{
    const int port = 80;
    if (!client.connect(host, port))
    {
        Serial.println("connection failed");
        return false;
    }

    Serial.print("Requesting URL: ");
    Serial.println(url);

    client.print(String("GET ") + url + " HTTP/1.1\r\n" + // 요청 라인
                "Host: " + host + "\r\n" + // 헤더
                "Connection: close\r\n\r\n"); // 헤더와 바디는 공백 한줄

    /*
    client.println("Host: " + host);
    client.println("Connection: close");
    client.println();
    */

    return true;
}

void deserialize(String line)
{
    const int doc_size = 800;
    StaticJsonDocument<doc_size> doc;

    auto error = deserializeJson(doc, line);
    if (error)
    {
        Serial.print("deserializeJson() failed with code");
        Serial.println(error.c_str());
        return ;
    }

    String w_main = doc["weather"][0]["main"];
    double temp = doc["main"]["temp"].as<double>();
    double humi = doc["main"]["humidity"].as<double>();

    String msg = "weather: " + w_main;
    com.print(0, msg.c_str());
    msg = String("T:") + temp + " H:" + humi;
    com.print(1, msg.c_str());
}

String response(WiFiClient& client)
{
    int timeout = millis() + 5000;

    while (!client.available())
    {
        if (timeout - millis() < 0)
        {
            Serial.println(">>> Client Timeout !");
            client.stop();
            return "";
        }
    }

    bool isBody = false;
    String body = "";

    while (client.available())
    {
        String line = client.readStringUntil('\r');
        line.trim();
        if (line == "")
        {
            isBody = true;
            continue ;
        }
        Serial.println(line);
        if (isBody)
        {
            body = line;
            break ;
        }
    }
    Serial.println();
    Serial.println("closing connection");
    return body;
}

void setup()
{
	com.init(ssid, password);
}

void loop()
{
	com.run();
	
    WiFiClient client;
    if (request(client))
    {
        String body = response(client);
        deserialize(body);
    }
    delay(100000);
}
