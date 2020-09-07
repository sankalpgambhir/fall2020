/*
Lab 1
Arduino Basics
*/

// variables

// functions
inline void test();

void setup(){
    Serial.begin(9600);
    pinMode(LED_BUILTIN, OUTPUT);
}

inline void test(){
    digitalWrite(LED_BUILTIN, LOW);
    Serial.print('0');
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.print('1');
    Serial.print("Game Over");
}
