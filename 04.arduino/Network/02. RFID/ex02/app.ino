#include <SPI.h>
#include <MFRC522.h>
#include <Buzzer.h>

const int rst_pin = 9;
const int ss_pin = 10;

MFRC522 mfrc(ss_pin, rst_pin);
Buzzer red(6);
Buzzer green(7);
byte myId[] = { 221, 38, 90, 211 };

void PrintUid()
{
    Serial.print("Card UID: ");
    for (byte i = 0; i < 10; ++i)
    {
        Serial.print(mfrc.uid.uidByte[i]);
        Serial.print(" ");
    }
    Serial.println();
}

boolean IsRegisteredId(byte *id)
{
    for (int i = 0; i < 4; ++i)
        if (myId[i] != id[i])
            return false;
    return true;
}

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
    PrintUid();

    if (IsRegisteredId(mfrc.uid.uidByte))
        green.beep(1000);
    else
        red.beep(1000);
}
