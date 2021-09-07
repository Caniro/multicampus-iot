#include <iostream>
#include "Car.hpp"

int main() {
    Car myCar;

    myCar.setSpeed(100);
    cout << "속도 : " << myCar.getSpeed() << endl;
}
