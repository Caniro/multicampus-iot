/*
    소리 센서 (KY-037)
    소리의 크기에 따라 PWM LED 출력
*/

#include <Analog.h>
#include <MiniCom.h>
#include <PWMLed.h>

MiniCom com;
Analog sound(A0, 0, 1023);
PWMLed led(9);

void check()
{
    int value = sound.read();
    value -= 519;
    value = map(value, 0, 4, 0, 255);
    com.print(1, "Value: ", value);
    led.setValue(value);
}

void setup()
{
    com.init();
    com.print(0, "[[Sound]]");
    com.setInterval(100, check);
}

void loop()
{
    com.run();
}
