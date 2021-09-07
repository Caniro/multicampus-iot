#include <Led.h>

#define OFF 0
#define ON 1

const int sw_pin = 2;
Led led(8);
boolean led_st = OFF;
int count = 0;

void onClick();

void setup() {
    Serial.begin(115200);
    pinMode(sw_pin, INPUT_PULLUP);
    led.setValue(led_st);
}

void loop() {
    boolean o_sw, n_sw;
    o_sw = !digitalRead(sw_pin);
    delay(10);
    n_sw = !digitalRead(sw_pin);
    
    if (o_sw == OFF && n_sw == ON)
    {
        onClick();
    }
}

void onClick()
{
    ++count;
    Serial.println(count);
    led_st = !led_st;
    led.setValue(led_st);
}
