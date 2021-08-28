/*
	웹서버 테스트
*/
#include <WifiMiniCom.h>

const char *ssid = "HanGuest1";
const char *password = "00001234";
WifiMiniCom com;
WiFiServer server(80);

void setup()
{
	com.init(ssid, password);
	server.begin();
}

void loop()
{
	com.run();
	
	WiFiClient client = server.available();
	if (!client) return;
	
	Serial.println("new client");
	while (!client.available())
		delay(1);
	
	String request = client.readStringUntil('\r'); // 첫 요청라인만 읽음
	Serial.println(request);
	client.flush(); // 요청 헤더와 바디 버림
	client.println("HTTP/1.1 200 OK");
	client.println("Content-type: text/html");
	client.println("");
	client.println("<!DOCTYPE HTML>");
	client.println("<html>");
	client.print("Hello World!");
	client.println("</html>");
	delay(1);
	Serial.println("Client disconnected");
	Serial.println("");
}
