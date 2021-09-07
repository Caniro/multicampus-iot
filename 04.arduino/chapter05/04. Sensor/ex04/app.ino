// SW-520D 기울기 센서
#include <Led.h>

Led led(9);
const int tilt_pin = 3;

void setup()
{
    pinMode(tilt_pin, INPUT_PULLUP);
}

void loop()
{
    boolean t_sw1, t_sw2;

    t_sw1 = digitalRead(tilt_pin);
    delay(200);
    t_sw2 = digitalRead(tilt_pin);

    if (t_sw1 == LOW && t_sw2 == HIGH)
        led.toggle();
}
