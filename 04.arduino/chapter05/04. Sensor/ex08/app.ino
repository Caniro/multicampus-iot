// Ultra, Buzzer 클래스를 사용하여 자동차 후방 감지기 모방
#include <MiniCom.h>
#include <Ultra.h>
#include <Buzzer.h>

MiniCom com;
Ultra ultra(5, 6);
Buzzer buzzer(7);

int off_times[] = { 0, 100, 200, 500, 1000 };

void check()
{
    int distance = ultra.getDistance();
    com.print(1, "Dist.(cm)=", distance);

    if (distance > 0 && distance < 50)
    {
        int ix = map(distance, 1, 50, 0, 4);
        buzzer.setOffTime(off_times[ix]);
    }
    else
        buzzer.stop();
}

void setup()
{
    com.init();
    com.setInterval(100, check);
    com.print(0, "[[Distance]]");
    buzzer.stop();
}

void loop()
{
    com.run();
    buzzer.run();
}
