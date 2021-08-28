/*
    EEPROM 사용 예제
*/

#include <EEPROM.h>

int randomNumber;

void setup()
{
    Serial.begin(115200);
    randomSeed(analogRead(0));
}

void loop()
{
    Serial.println("Writing random numbers...");

    for (int i = 0; i < 10; ++i)
    {
        randomNumber = random(256);
        EEPROM.write(i, randomNumber);
        delay(100);
    }

    Serial.println("");

    for (int i = 0; i < 10; ++i)
    {
        int num = EEPROM.read(i);
        Serial.println("EEPROM Address : " + String(i) +
            + "\t, Value : " + num);
        delay(100);
    }

    while(true);
}
