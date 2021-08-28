#include <ESP8266WiFi.h>
#include <MiniCom.h>

const char *ssid = "HanGuest1";
const char *password = "00001234";
MiniCom com;

void wifi_connect()
{
	WiFi.begin(ssid, password); // 비밀번호가 없으면 password 자리에 NULL
	com.print(0, "try to connect");
	Serial.println();
	while (WiFi.status() != WL_CONNECTED)
	{
		delay(500);
		Serial.print(".");
	}
	
	com.print(0, "WiFi connected");
	com.print(1, WiFi.localIP().toString().c_str());
	Serial.println();
	Serial.println(WiFi.localIP());
}

void setup()
{
	com.init();
	wifi_connect();
}

void loop()
{
	com.run();
}
