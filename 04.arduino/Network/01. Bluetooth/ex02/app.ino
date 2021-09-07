// on, off 가 전송되면 LED 켜고끄기
#include <SoftwareSerial.h>
#include <MiniCom.h>
#include <Led.h>

MiniCom com;

SoftwareSerial BTSerial(13, 12); // 아두이노 측의 rx, tx

String myString="";
int count = 0;
Led led(8);

void setup()
{
    com.init();
    com.print(0, "[[Bluetooth]]");
    BTSerial.begin(9600);
}

void loop()
{
    while (BTSerial.available())
    {
        char myChar = (char)BTSerial.read();
        myString += myChar;
        delay(5);
    }

    if (!myString.equals(""))
    {
        myString.trim();
        if (myString == "on")
            led.on();
        else if (myString == "off")
            led.off();
        char buf[17];
        sprintf(buf, "%d)%s", ++count, myString.c_str());
        com.print(1, buf);
        BTSerial.println("input value: " + myString);
        myString = "";
    }
}
