#include <Led.h>

int led_pin = 9;
Led led(led_pin);

void setup() {}

void loop()
{
    int pwm_val = 0;
    for (; pwm_val < 200; pwm_val += 5)
    {
        analogWrite(led_pin, pwm_val);
        delay(100);
    }
    for (; pwm_val >= 0; pwm_val -= 5)
    {
        analogWrite(led_pin, pwm_val);
        delay(100);
    }

    led.off();
    delay(2000);
}
