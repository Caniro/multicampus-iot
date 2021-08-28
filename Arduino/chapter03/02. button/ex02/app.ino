#include <Led.h>

const int in_pu_sw_pin = 2;
Led led(12);

void setup() {
    pinMode(in_pu_sw_pin, INPUT_PULLUP);
}

void loop() {
    boolean in_pu_sw;
    in_pu_sw = !digitalRead(in_pu_sw_pin); // 풀업 -> 풀다운 변환
    led.setValue(in_pu_sw);
}
