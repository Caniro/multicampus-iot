/*
    문제
    블루투스 통신으로 서보 모터 제어
    "open" : 서보 모터 90도 회전
    "close" : 서보 모터 0도 회전
*/
#include <BtMiniCom.h>
#include <Servo.h>

void receive_msg(String msg);

BtMiniCom com(13, 12, receive_msg);
int count = 0;
Servo servo;

void receive_msg(String msg)
{
    String result("");

    if (msg == "open")
    {
        servo.write(90);
        result = "OK(open)";
    }
    else if (msg == "close")
    {
        servo.write(0);
        result = "OK(close)";
    }
    else
        result = "Fail(" + msg + ")";

    char buf[17];
    sprintf(buf, "%d)%s", ++count, msg.c_str());
    com.print(1, buf);
    com.send(result);
}

void setup()
{
    com.init();
    com.print(0, "[[Bluetooth]]");
    servo.attach(3);
    servo.write(0);
}

void loop()
{
   com.run(); 
}
