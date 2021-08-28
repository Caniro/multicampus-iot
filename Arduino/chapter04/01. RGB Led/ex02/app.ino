#include <ColorLed.h>

ColorLed led(9, 10, 11);

void setup()
{
    Serial.begin(115200);
}

void loop()
{
    led.random();
    delay(500);
    pwm_one_color();
    pwm_two_color();
    pwm_three_color();
}

void led_off(int d_time=1000)
{
    delay(d_time);
    led.off(d_time);
    Serial.println("--------------------------");
}

void pwm_one_color()
{
    Serial.println("R PWM OUTPUT");
    for (int r = 0; r <= 255; r += 50)
    {
        led.rgb(r, 0, 0);
        delay(500);
    }
    led_off();
    Serial.println("--------------------------");

    Serial.println("G PWM OUTPUT");
    for (int g = 0; g <= 255; g += 50)
    {
        led.rgb(0, g, 0);
        delay(500);
    }
    led_off();
    
    Serial.println("B PWM OUTPUT");
    for (int b = 0; b <= 255; b += 50)
    {
        led.rgb(0, 0, b);
        delay(500);
    }
    led_off();
    Serial.println("--------------------------");
}

void pwm_two_color()
{
    Serial.println("RG PWM OUTPUT");
    for (int r = 0; r <= 255; r += 50)
        for (int g = 0; g <= 255; g += 50)
        {
            led.rgb(r, g, 0);
            delay(500);
        }
    led_off();
    Serial.println("--------------------------");

    Serial.println("GB PWM OUTPUT");
    for (int g = 0; g <= 255; g += 50)
        for (int b = 0; b <= 255; b += 50)
        {
            led.rgb(0, g, b);
            delay(500);
        }
    led_off();
    Serial.println("--------------------------");
    
    Serial.println("BR PWM OUTPUT");
    for (int b = 0; b <= 255; b += 50)
        for (int r = 0; r <= 255; r += 50)
        {
            led.rgb(r, 0, b);
            delay(500);
        }
    led_off();
    Serial.println("--------------------------");
}

void pwm_three_color()
{
    Serial.println("RGB PWM OUTPUT");
    for (int r = 0; r <= 255; r += 50)
        for (int g = 0; g <= 255; g += 50)
            for (int b = 0; b <= 255; b += 50)
            {
                led.rgb(r, g, 0);
                delay(500);
            }
    led_off();
    Serial.println("--------------------------");
}
