#include "Led.h"

Led led[4] = { Led(3), Led(4), Led(5), Led(6) };

int out_no = 0;

void setup() {}

void loop() {
    led[out_no].toggle();
    delay(1000);
    led[out_no].toggle();
    out_no = (out_no + 1) % 4;
}
