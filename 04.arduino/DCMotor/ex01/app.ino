int ENAPin = 9;
int in1Pin = 8;
int in2Pin = 7;

int ENBPin = 3;
int in3Pin = 5;
int in4Pin = 4;

void setup()
{
    pinMode(in1Pin, OUTPUT);
    pinMode(in2Pin, OUTPUT);
    pinMode(in3Pin, OUTPUT);
    pinMode(in4Pin, OUTPUT);

    analogWrite(ENAPin, 200);
    analogWrite(ENBPin, 200);
}

void loop()
{
    // 전진
    digitalWrite(in1Pin, HIGH);
    digitalWrite(in2Pin, LOW);
    digitalWrite(in3Pin, HIGH);
    digitalWrite(in4Pin, LOW);
    delay(2000);

    // 후진
    digitalWrite(in1Pin, LOW);
    digitalWrite(in2Pin, HIGH);
    digitalWrite(in3Pin, LOW);
    digitalWrite(in4Pin, HIGH);
    delay(2000);

    // 정지
    digitalWrite(in1Pin, LOW);
    digitalWrite(in2Pin, LOW);
    digitalWrite(in3Pin, LOW);
    digitalWrite(in4Pin, LOW);
    delay(2000);

    // 좌회전 (L: 후진, R: 전진)
    digitalWrite(in1Pin, LOW);
    digitalWrite(in2Pin, HIGH);
    digitalWrite(in3Pin, HIGH);
    digitalWrite(in4Pin, LOW);
    delay(2000);

    // 우회전 (L: 전진, R: 후진)
    digitalWrite(in1Pin, HIGH);
    digitalWrite(in2Pin, LOW);
    digitalWrite(in3Pin, LOW);
    digitalWrite(in4Pin, HIGH);
    delay(2000);

    // 정지
    digitalWrite(in1Pin, LOW);
    digitalWrite(in2Pin, LOW);
    digitalWrite(in3Pin, LOW);
    digitalWrite(in4Pin, LOW);
    delay(2000);
}
