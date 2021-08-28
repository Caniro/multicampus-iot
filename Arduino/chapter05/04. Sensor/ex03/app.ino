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
    led.setValue(digitalRead(tilt_pin));
}
