/*
Lab 2
PWM
*/
#define SIZE 1000

// variables
uint16_t timeseries[SIZE];
int i;

// functions

void setup(){
    Serial.begin(1000000); // why not
    pinMode(11, OUTPUT);
    pinMode(A0, INPUT);
    analogWrite(11, 100);
    i = 0;
}

void loop(){
  if(i == SIZE){
    for(int j=0; j<i;j++){
        Serial.print(timeseries[j]);
        Serial.print(' ');
      }
    i = 0;
    Serial.print('\n');
    }
  else{
    timeseries[i] = analogRead(A0);
    i++;
  }
}