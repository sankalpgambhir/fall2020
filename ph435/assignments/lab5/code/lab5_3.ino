/*
Lab 5.420
Delay measuring with interrupts
*/

#include "TimerOne.h"

#define InPin(x) 3-x

// Declaring global variables
long long dt; 
long long diffMax;
const int measureTime = 10;

// functions
void phaseCheck();

void setup() {

  Serial.begin(9600); // why not

  Timer1.initialize(measureTime);
  Timer1.attachInterrupt(phaseCheck);

  pinMode(InPin(0), INPUT);
  pinMode(InPin(1), INPUT);

  attachInterrupt(digitalPinToInterrupt(InPin(0)), 
                    [](void){edgeCount++;}, 
                    FALLING);

  attachInterrupt(digitalPinToInterrupt(InPin(0)), 
                    [](void){diff = 1;}, 
                    FALLING); // edge counting
  attachInterrupt(digitalPinToInterrupt(InPin(1)), 
                    [](void){diff = 0;}, 
                    FALLING);

  dt = diff = diffMax = 0;
}

void loop() {
    Serial.print("Max delay measured");
    Serial.print(diffMax);
    Serial.print(" uS\n");
}

void setup() {// put your setup code here, to run once:
  Serial.begin(9600);
  Timer1.initialize(t_period);
  Timer1.attachInterrupt(phase_detect);
  attachInterrupt(digitalPinToInterrupt(input_pin_1), [](){diff = 1;}, FALLING); // interrupt
  attachInterrupt(digitalPinToInterrupt(input_pin_2), [](){diff = 0;}, FALLING); // interrupt
  pinMode(input_pin_1, INPUT);
  pinMode(input_pin_2, INPUT);
  diff_count = 0;
  del_t = 0;

}

void loop() {
    Serial.print(diffMax);
    Serial.println(" uS");
    delay(output_period);
     
}

void checkPhase(){
  if( diff == 1 ){         
    dt += measureTime;         
  }                                   
  if ( (diff == 0) && (del_t != 0) ){
    diffMax = diffMax > dt ? diffMax : dt;
    dt = 0;  
  }
  
}