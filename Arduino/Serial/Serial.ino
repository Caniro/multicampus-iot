int rec_byte;

void setup() {
    Serial.begin(115200);
}

void loop() {
    if (Serial.available() > 0)
    {
      rec_byte = Serial.read();
      Serial.write(rec_byte);
    }
}
