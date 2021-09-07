#include <SPI.h>
#include <MFRC522.h>
#include <Buzzer.h>

const int rst_pin = 9;
const int ss_pin = 10;

MFRC522 mfrc(ss_pin, rst_pin);
Buzzer led(8);

void setup()
{
    Serial.begin(115200);
    SPI.begin();
    mfrc.PCD_Init();
}

void loop()
{
    if (!mfrc.PICC_IsNewCardPresent() || !mfrc.PICC_ReadCardSerial())
    {
        delay(500);
        return ;
    }
    
    led.beep();
    Serial.print("Card UID: ");

    for (byte i = 0; i < 10; ++i)
    {
        Serial.print(mfrc.uid.uidByte[i]);
        Serial.print(" ");
    }
    Serial.println();
}
