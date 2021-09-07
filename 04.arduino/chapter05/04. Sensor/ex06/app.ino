// 초음파 센서
#include <MiniCom.h>

MiniCom com;

int echoPin = 5;
int triggerPin = 6;

void check()
{
    digitalWrite(triggerPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(triggerPin, LOW);

    int distance = pulseIn(echoPin, HIGH) / 58; // 0.017 * 시간
    com.print(1, "Dist.(cm)=", distance);
}

void setup()
{
    com.init();
    com.setInterval(100, check);
    com.print(0, "[[Distance]]");
    pinMode(triggerPin, OUTPUT);
    pinMode(echoPin, INPUT);
}

void loop()
{
    com.run();
}
