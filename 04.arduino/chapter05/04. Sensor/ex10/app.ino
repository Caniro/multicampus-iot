/*
    진입 차단기 모방 문제점 개선
    1. 서보모터 전력 -> 서보모터를 Vin에 연결(USB 연결 시)...왜계속돌지
    2. 너무 많은 계산량 -> setInterval
*/

#include <MiniCom.h>
#include <Ultra.h>
#include <Servo.h>

MiniCom com;
Ultra ultra(5, 6);
Servo servo;

void open()
{
    com.print(1, "Open");
    servo.write(90);
}

void close()
{
    com.print(1, "Close");
    servo.write(0);
}

void check()
{
    int distance = ultra.run();
    com.print(1, "Dist.(cm)=", distance);
}

void setup()
{
    com.init();
    com.print(0, "[[Distance]]");
    com.setInterval(100, check);
    ultra.setThreshold(40, open, close);
    servo.attach(3);
    close();
}

void loop()
{
    com.run();
}
