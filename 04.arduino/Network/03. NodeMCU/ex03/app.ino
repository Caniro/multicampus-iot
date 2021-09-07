/*
	WifiMiniCom 클래스화
	업로드 후 터미널에서 ping IP 명령어로 연결 체크해보기
*/
#include <WifiMiniCom.h>

const char *ssid = "HanGuest1";
const char *password = "00001234";
WifiMiniCom com;

void setup()
{
	com.init(ssid, password);
}

void loop()
{
	com.run();
}
