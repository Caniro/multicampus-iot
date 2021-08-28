#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
    lcd.init();
    lcd.backlight();
    lcd.setCursor(0,0);
    lcd.print("1++++++++23---------------45****");
    lcd.setCursor(0,1);
    lcd.print("1++++++++23---------------45****");
}
void loop() {
    for (int n = 0; n < 80; n ++)
    {
        lcd.scrollDisplayLeft();
        delay(100);
    }
    delay(1000);
    for (int n = 0; n < 80; n ++)
    {
        lcd.scrollDisplayRight();
        delay(100);
    }
    delay(1000);
}
