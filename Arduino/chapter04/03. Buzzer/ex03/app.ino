#include <Melody.h>
#include "mario.h"

const int speaker_pin = 9;

Melody melody(speaker_pin, notes, durations, 
            sizeof(notes) / sizeof(notes[0]));

void setup()
{
    melody.play();
}

void loop()
{
    melody.run();
}
