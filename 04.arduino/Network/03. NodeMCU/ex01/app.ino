// NodeMCU 연결 테스트
void setup()
{
	Serial.begin(115200);
}

void loop()
{
	Serial.println("Hello");
    delay(2000);
}
