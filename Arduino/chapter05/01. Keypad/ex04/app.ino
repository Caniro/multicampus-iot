/*
    문제 - 도어락 인터페이스2
    * : 시작, LCD에 Start 출력
    숫자 입력 - 안보여줌
    # : 키 입력 종료, LCD에 입력한 정보 출력
    3초간 입력 없을 경우 리셋
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
int timerId = -1;

void setup()
{
    com.init();
    com.print(0, "[[Keypad Test]]");
}

void loop()
{
    com.run();
    char key = keypad.getKey();

    if (key)
        process(key);
}

void process(char key)
{
    SimpleTimer& timer = com.getTimer();

    if (key == '*' && b_input == false)
    {
        b_input = true;
        input = "";
        com.print(1, "Start");
        timerId = timer.setTimeout(3000, reset);
        tick();
    }
    else if (key == '#')
    {
        timer.deleteTimer(timerId);
        b_input = false;
        check();
        tick();
    }
    else if (b_input)
    {
        timer.restartTimer(timerId);
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

void reset()
{
    com.print(1, "Reset");
    input = "";
    b_input = false;
    tick();
    tick();
    tick();
}
