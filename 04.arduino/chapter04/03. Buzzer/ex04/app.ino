#include <Melody.h>
#include <MiniCom.h>
#include <Button.h>
#include "mario.h"

const int speaker_pin = 9;
const int button_pin = 2;
MiniCom com;
Button btn(button_pin);
Melody melody(speaker_pin, notes, durations, 
            sizeof(notes) / sizeof(notes[0]));

void check()
{
    bool bplay = melody.toggle(true);
    if (bplay)
        com.print(0, "play");
    else
        com.print(0, "pause");
}

void setup()
{
    com.init();
    btn.setCallback(check);
    melody.play();
    com.print(0, "play");
}

void loop()
{
    com.run();
    melody.run();
    btn.check();
}
