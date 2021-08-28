// 진입 차단기 모방
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

void setup()
{
    com.init();
    com.print(0, "[[Distance]]");
    ultra.setThreshold(40, open, close);
    servo.attach(4);
}

void loop()
{
    com.run();
    ultra.run();
}

/*
    문제점
    1. 서보모터 전력
    2. 너무 많은 계산량
*/
