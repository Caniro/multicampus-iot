#pragma once

#include <string>
using namespace std;

class Car {
protected:
    int speed;
    int gear;
    string color;
public:
    Car();
    ~Car();
    int getSpeed();
    void setSpeed(int s);
};
