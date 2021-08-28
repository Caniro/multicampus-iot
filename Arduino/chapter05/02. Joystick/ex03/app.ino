/*
    문제
    조이스틱 x값으로 서보모터 각도 조정
        LCD 각도 표시
    조이스틱 버튼 누르면 서보모터 각도 고정
        LCD에 LOCK, 각도 표시
    버튼 다시 누르면 각도 고정 해제
*/

#include <Servo.h>
#include <MiniCom.h>
#include <Analog.h>
#include <Button.h>

MiniCom com;
Analog x(A1, 0, 180);
Button btn(A0);
Servo servo;

boolean lock = false;
int lock_angle = 0;

void btn_on_click()
{
    lock = !lock;
    if (lock)
    {
        lock_angle = x.read();
        servo.write(lock_angle);
    }
}

void check()
{
    int dx;
    boolean sw;

    dx = x.read();
    
    char buf[17];
    if (lock)
        sprintf(buf, "Lock %3d", lock_angle);
    else
    {
        servo.write(dx);
        sprintf(buf, "Angle %3d", dx);
    }
    com.print(1, buf);
}

void setup()
{
    com.init();
    com.setInterval(100, check);
    com.print(0, "[[Joystick]]");
    servo.attach(7);
    btn.setCallback(btn_on_click);
}

void loop()
{
    com.run();
    btn.check();
}
