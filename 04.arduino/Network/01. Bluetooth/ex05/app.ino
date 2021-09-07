/*
    문제
    블루투스 통신으로 서보 모터 제어
    EEPROM에 저장된 비밀번호와 일치하면 open
*/
#include <BtMiniCom.h>
#include <Servo.h>
#include <storage.h>

void receive_msg(String msg);

BtMiniCom com(13, 12, receive_msg);
int count = 0;
Servo servo;

void receive_msg(String msg)
{
    String result("");
    String input_pw("");

    if (msg.startsWith("doorlock "))
        input_pw = msg.substring(strlen("doorlock "));
    if (input_pw == readRom(100))
    {
        servo.write(90);
        result = "OK(open)";
        com.getTimer().setTimeout(5000, [](){servo.write(0);});
    }
    else
    {
        servo.write(0);
        result = "Fail(" + msg + ")";
    }

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
