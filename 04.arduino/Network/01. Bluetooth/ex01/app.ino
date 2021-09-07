#include <SoftwareSerial.h>
#include <MiniCom.h>

MiniCom com;

SoftwareSerial BTSerial(13, 12); // 아두이노 측의 rx, tx

String myString="";
int count = 0;

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
        char buf[17];
        sprintf(buf, "%d)%s", ++count, myString.c_str());
        com.print(1, buf);
        BTSerial.println("input value: " + myString);
        myString = "";
    }
}
