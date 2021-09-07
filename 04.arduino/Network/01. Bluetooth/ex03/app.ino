// BtMiniCom 클래스

#include <BtMiniCom.h>
#include <Led.h>

void receive_msg(String msg);

BtMiniCom com(13, 12, receive_msg);
Led led(8);
int count = 0;

void receive_msg(String msg)
{
    String result("");

    if (msg == "on")
    {
        led.on();
        result = "OK(on)";
    }
    else if (msg == "off")
    {
        led.off();
        result = "OK(off)";
    }
    else
        result = "Fail(" + msg + ")";

    char buf[17];
    sprintf(buf, "%d)%s", ++count, msg.c_str());
    com.print(1, buf);
    // com.send("input value: " + msg);
    com.send(result);
}

void setup()
{
    com.init();
    com.print(0, "[[Bluetooth]]");
}

void loop()
{
   com.run(); 
}
