const int sw_pin = 2;
int count = 0;

int t1, t2;

void flash(void)
{
    t2 = millis();

    if (t2 - t1 < 200) return;
    else t1 = t2;

    ++count;
    Serial.println(count);
}

void setup()
{
    Serial.begin(115200);
    pinMode(sw_pin, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(sw_pin), flash, FALLING);

    t1 = millis();
    Serial.println(t1);
}

void loop() {}
