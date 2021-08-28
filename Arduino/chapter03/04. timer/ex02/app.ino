#include <Led.h>
#include <SimpleTimer.h>

SimpleTimer timer;

Led leds[] {
    Led(8), Led(9)
};

void setup()
{
    timer.setInterval(1000, blink0);
    timer.setInterval(500, blink1);
}

void loop() {
    timer.run();
}

void blink0()
{
    leds[0].toggle();
}

void blink1()
{
    leds[1].toggle();
}
