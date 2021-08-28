/*
    소리 센서 (KY-037)
*/

#include <Analog.h>
#include <MiniCom.h>

MiniCom com;
Analog sound(A0, 0, 1023);

void setup()
{
    com.init();
    com.print(0, "[[Sound]]");
    com.setInterval(100, check);
}

void check()
{
    int value = sound.read();
    com.print(1, "Value: ", value);
}

void loop()
{
    com.run();
}
