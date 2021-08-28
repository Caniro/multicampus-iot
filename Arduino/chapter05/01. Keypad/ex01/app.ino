#include <MiniCom.h>
#include <Keypad.h>
#include "Keymap.h"

MiniCom com;
Keypad keypad(Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS));
String input("");

void setup()
{
    com.init();
    com.print(0, "[[Keypad Test]]");
}

void loop()
{
    char key = keypad.getKey();

    if (key)
    {
        input += key;
        com.print(1, input.c_str());
    }
}
