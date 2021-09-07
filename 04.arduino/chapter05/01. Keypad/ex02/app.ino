/*
    문제 - 도어락 인터페이스1
    * : 시작, LCD에 Start 출력
    숫자 입력 - 안보여줌, 소리내고 LED
    # : 키 입력 종료, LCD에 입력한 정보 출력
*/

#include <MiniCom.h>
#include <Keypad.h>
#include <Led.h>
#include "Keymap.h"

MiniCom com;
Keypad keypad(Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS));
String input("");
boolean b_input = false;
Led beep(13);

void setup()
{
    com.init();
    com.print(0, "[[Keypad Test]]");
}

void loop()
{
    char key = keypad.getKey();

    if (key)
        process(key);
}

void process(char key)
{
    if (key == '*' && b_input == false)
    {
        b_input = true;
        input = "";
        com.print(1, "Start");
    }
    else if (key == '#')
    {
        b_input = false;
        check();
    }
    else if (b_input)
    {
        input += key;
        tick();
    }
}

void check()
{
    com.print(1, input.c_str());
    delay(3000);
    com.print(1, "");
}

void tick()
{
    beep.on();
    delay(100);
    beep.off();
}
