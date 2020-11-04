/*
Lab 5
Interrupt based DSO
*/

#include "TimerOne.h"

#define InPin(x) 3-x

// Declaring global variables
volatile float freq; 
volatile int edgeCount; 
long long int dt; 
const int measureTime = 5000;
const int minEdges = 5000; 
const int outTime = 500;

// functions
void checkFreq();

void setup() {

  Serial.begin(9600); // why not

  Timer1.initialize(measureTime);
  Timer1.attachInterrupt(checkFreq);

  pinMode(InPin(0), INPUT);
  pinMode(InPin(1), INPUT);

  attachInterrupt(digitalPinToInterrupt(InPin(0)), 
                    [](void){edgeCount++;}, 
                    FALLING);

  freq = dt = edgeCount = 0;
}

void loop() {
    Serial.println(edgeCount);
    delay(outTime); 
}

void checkFreq(){
  dt += measureTime/1000.0;
  if(edgeCount >= minEdges){ 
    freq = (edgeCount*1000.0)/(double)dt;
    edgeCount = 0; 
    dt = 0;
  }  
}