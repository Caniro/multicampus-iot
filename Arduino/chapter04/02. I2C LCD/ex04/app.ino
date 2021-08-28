#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

const int num_char = 3;
// https://maxpromer.github.io/LCD-Character-Creator/
byte customChar[num_char][8] = {
    {B01010,B11110,B01011,B10110,B01010,B00010,B01000,B01110},
    {B00000,B00100,B01010,B00100,B00000,B11111,B01010,B01010},
    {B00001,B01011,B10101,B01011,B00001,B01110,B01110,B01110}
};

void setup() {
    lcd.init();
    for (int i = 0; i < num_char; ++i)
        lcd.createChar(i, customChar[i]);
    lcd.backlight();
    lcd.setCursor(0,0);
    lcd.write(0);
    lcd.setCursor(1,0);
    lcd.write(1);
    lcd.setCursor(2,0);
    lcd.write(2);
}
void loop() {}
