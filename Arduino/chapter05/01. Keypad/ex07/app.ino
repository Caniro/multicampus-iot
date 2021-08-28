/*
    문제 - 도어락 인터페이스4
    * : 시작
    숫자 입력 시 마다 LCD에 * 출력
    # : 키 입력종료, LCD 클리어
    3초간 입력 없을 경우 리셋
    평소엔 LCD 끄고 있기 -> MiniCom 클래스에 메서드 추가
    비밀번호 EEPROM에 저장
*/

#include <MiniCom.h>
#include <Keypad.h>
#include <Servo.h>
#include <Led.h>
#include <storage.h>
#include "Keymap.h"

MiniCom com;
Keypad keypad(Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS));
String input("");
String inputStar("");
String password = "";
boolean b_input = false;
Led beep(13);
int timerId = -1;
Servo lock;
int servo_pin = 3;

void setup()
{
    com.init();
    com.offLcd();
    com.print(0, "[[Door Lock]]");
    lock.attach(servo_pin);
    writeRom(100, "0000");
    password = readRom(100);
    Serial.println(String("Password : ") + password);
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
        inputStar = "";
        timerId = timer.setTimeout(3000, reset);
        tick();
        com.onLcd();
    }
    else if (key == '#')
    {
        timer.deleteTimer(timerId);
        b_input = false;
        check();
        com.offLcd();
    }
    else if (b_input)
    {
        timer.restartTimer(timerId);
        input += key;
        inputStar += '*';
        tick();
    }
    com.print(1, inputStar.c_str());
}

void check()
{
    if (input == password)
    {
        lock.write(90);
        delay(5000);
        lock.write(0);
    }
    else
    {
        tick(4);
        inputStar = "";
    }
}

void reset()
{
    input = "";
    inputStar = "";
    b_input = false;
    tick(3);
    com.print(1, inputStar.c_str());
    com.offLcd();
}

void tick()
{
    beep.on();
    delay(100);
    beep.off();
    delay(50);
}

void tick(int n)
{
    for (int i = 0; i < n; ++i)
        tick();
}

void changePassword(const String& new_pw)
{

}