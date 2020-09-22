/*
Lab 3
DAC
*/

// variables
uint8_t temp;

// functions

void setup(){
    Serial.begin(1000000); // why not
    DDRD = 0b11111110; // pins 1-7 as output. 0 is Tx
    temp = 0b00000000; // initialise as low 
    PORTD = temp;
}

void loop(){
    // go from 0.9 to 2.2V
    // for temp from 12 to 28 adding 4, in binary to be explicit about pins
    for(temp = 0b00001100; temp <= 0b00011100; temp += 0b100){
      PORTD = temp;
      delay(500);
    }
}