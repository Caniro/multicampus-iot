#include <Servo.h>
#include <MiniCom.h>

MiniCom com;
Servo myServo;
const int servo_pin = 3;

void setup()
{
    com.init();
    com.print(0, "Servo Test");
    myServo.attach(servo_pin);
}

void move_angle(int angle, int delay_time)
{
    myServo.write(angle);
    delay(delay_time);
    com.print(1, "Angle:", angle);
}

void loop()
{
    move_angle(0, 1000);
    move_angle(90, 1000);
    move_angle(180, 1000);
    move_angle(90, 1000);
}
