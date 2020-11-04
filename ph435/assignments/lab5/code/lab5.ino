/*
Lab 5
Interrupt based DSO
*/

#include <TimerOne.h>


// global params
#define minEdges 5000
#define measureTime int(1e7) // us
  // pins
#define sourcePin(x) x+2

// variables
float freq = 0;
volatile long edgeCount[2] = {0, 0};
volatile bool toReport = false;

// functions
  // use lambdas for interrupts


void setup() {
  Serial.begin(9600); // why not

  Timer1.initialize(measureTime);
  Timer1.attachInterrupt([](void){toReport = true;}, measureTime); // timer


  pinMode(sourcePin(0), 0);
  pinMode(sourcePin(1), 0);

  attachInterrupt(digitalPinToInterrupt(sourcePin(0)), 
                    [](void){edgeCount[0]++;}, 
                    FALLING); // edge counting
  attachInterrupt(digitalPinToInterrupt(sourcePin(1)), 
                    [](void){edgeCount[1]++;}, 
                    FALLING);

}

void loop() {
  Serial.println("Working..");
  Serial.println(toReport);

  if(toReport){

  noInterrupts(); // lock volatiles

  // after no interrupt there is only calculation, no delay etc

  if(edgeCount[0] < minEdges){
    Serial.println("Not enough data!");
  } 
  else{
    freq = (edgeCount[0] / float(measureTime)) * 1e6F;
    Serial.print("Frequency: ");
    Serial.print(freq);
    Serial.print(" Hz.\n");
    edgeCount[0] = 0;
  }

  toReport = false;

  interrupts(); // free

  }
} 