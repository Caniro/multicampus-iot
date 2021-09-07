/*
    문제
    버튼을 한 번 누르면 서보 모터 90도 회전
    한번 더 누르면 0도 회전
*/

#include <Button.h>
#include <Servo.h>
#include <MiniCom.h>

Button btn(2);
MiniCom com;
Servo myServo;
const int servo_pin = 5;
boolean bOpen = false;

void open()
{
    myServo.write(0);
    com.print(1, "Open");
}

void close()
{
    myServo.write(90);
    com.print(1, "Close");
}

void check()
{
    bOpen = !bOpen;
    if (bOpen)
        open();
    else
        close();
}

void setup()
{
    com.init();
    com.print(0, "Servo Test3");
    myServo.attach(servo_pin);
    btn.setCallback(check);
    close();
}

void loop()
{
    com.run();
    btn.check();
}
