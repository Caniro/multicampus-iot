const int led_pin[4] = {3, 4, 5, 6};

const int led_out[4][4] = {
    {1, 0, 0, 0},
    {0, 1, 0, 0},
    {0, 0, 1, 0},
    {0, 0, 0, 1},
};

int out_no = 0;

void setup()
{
    for (int n = 0; n < 4; ++n)
    {
        pinMode(led_pin[n], OUTPUT);
        digitalWrite(led_pin[n], LOW);
    }
}

void loop()
{
    for (int n = 0; n < 4; ++n)
    {
        // digitalWrite(led_pin[n], led_out[out_no][n]);
        digitalWrite(led_pin[n], n == out_no);
    }
    // ++out_no;
    // if (out_no == 4) out_no = 0;
    out_no = (out_no + 1) % 4;
    delay(1000);
}
