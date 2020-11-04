/*
Lab 4.20
Ping-Pong
With Physics
*/

// used pins
#define leftPlayer 2
#define rightPlayer 3
#define playerPin(x) (x + 5)
  // LED outputs
int redPin[4] = {5, 9, 10, 11}; // pins grouped by the same frequency
int grePin[2] = {7, 8}; // use playerPin(x) macro instead for compile time resolution


// variables
#define maxWait 1500
uint8_t state = 0; // start state
uint8_t ball[2] = {0, 1}; // position 0, moving right
uint8_t ballInRange = 0; // 0 = none, 1 = left, 2 = right
volatile bool leftHit = false, rightHit = false;
bool lightOn = 0;
uint16_t lightOnStart = 0;
unsigned long ballWaitStart = 0; // time ball has been near player
volatile uint16_t timeLeftHit = 0, timeRightHit = 0; 
uint16_t delayBySpeed = 600;
uint8_t victory = 0; // has a player won? if yes, which?

// functions
void leftPlayerHit();
void rightPlayerHit();
void changeOutputs();

void setup(){
    Serial.begin(1000000); // why not
    DDRD |= 0b11111110; // pins 1-7 as output. 0 is Tx
    DDRB |= 0b11111111; // set all pins 8-13 (and dummy bits) to output
    PORTD = 0x0;  // initialise as low 
    PORTB = 0x0;

    changeOutputs(); // initial lights
    pinMode(leftPlayer, INPUT);
    attachInterrupt(digitalPinToInterrupt(leftPlayer), leftPlayerHit, FALLING);
    pinMode(rightPlayer, INPUT);
    attachInterrupt(digitalPinToInterrupt(rightPlayer), rightPlayerHit, FALLING);
}

void loop(){

    Serial.println(state);

    if(lightOn){
      if((millis() - lightOnStart) >= 300){
        digitalWrite(playerPin(leftPlayer), 0);
        digitalWrite(playerPin(rightPlayer), 0);
      }
    }

    // reset interrupts if not handled
    if(leftHit){
      timeLeftHit++;
      if(timeLeftHit > 3){
        timeLeftHit = 0;
        leftHit = 0;
      }
    }

    if(rightHit){
      timeRightHit++;
      if(timeRightHit > 3){
        timeRightHit = 0;
        rightHit = 0;
      }
    }


    switch (state)
    {
    case 0:
      // initial state
      // wait for first input
      if(leftHit) {state = 1; leftHit = 0; ball[0] += ball[1]; changeOutputs();}
      break;

    case 1:
      // game in play
      delay(delayBySpeed); // delay to control clock speed
      if(ball[0] != 0 && ball[0] != 3){
        // somewhere in the middle
        ball[0] += ball[1]; // x = x + v.dt
        changeOutputs();
        break;
      }
      else{
        ballInRange = (ball[0] == 0) ? 1 : -1;
        state = (ball[0] == 0) ? 2 : 3;
        // start counter
        ballWaitStart = millis();
      }
    
    case 2:
      // ball in left range
      if((millis() - ballWaitStart) >= maxWait){
        victory = playerPin(rightPlayer);
        state = 4;
        break;
      }
      if(!leftHit) break;

      ball[1] = 1; // travel to right
      leftHit = false; // reset
      digitalWrite(playerPin(leftPlayer), 1); // light up
      lightOn = true; lightOnStart = millis();
      ball[0] += ball[1]; changeOutputs();
      delayBySpeed = 300 + (millis() - ballWaitStart > 700 ? 0 : 300);
      state = 1;
      break;
    
    case 3:
      // ball in right range
      if((millis() - ballWaitStart) >= maxWait){
        victory = playerPin(leftPlayer);
        state = 4;
        break;
      }
      if(!rightHit) break;

      ball[1] = -1; // travel to left
      rightHit = false; // reset
      digitalWrite(playerPin(rightPlayer), 1); // light up
      lightOn = true; lightOnStart = millis();
      ball[0] += ball[1]; changeOutputs();
      delayBySpeed = 300 + (millis() - ballWaitStart > 700 ? 0 : 300);
      state = 1;
      break;
    
    case 4:
      // ball miss
      // flash 4 times;
      for(int i = 1; i <= 8; i++){
        digitalWrite(victory, i%2);
        delay(250);
      }
      // go back to initial
      ball[0] = 0;
      ball[1] = 1;
      ballInRange = 0;
      state = 0;
      changeOutputs();
      break;
    
    default:
      Serial.println("Invalid state variable! Defaulting to initial.");
      ball[0] = 0;
      ball[1] = 1;
      ballInRange = 0;
      state = 0;
      break;
    }
}

void leftPlayerHit(){
  leftHit = true;
  timeLeftHit = 0;
  return;
}

void rightPlayerHit(){
  rightHit = true;
  timeRightHit = 0;
  return;
}

void changeOutputs(){
    int dir = (ball[1] > 0);
    for(int i = 0; i < 4; i++){
        if((ball[0] == i) || (ball[0] == (i - dir))){
            // leave a trail
            analogWrite(redPin[i], 255 * ((int) (ball[0] == i)));
        }
        else{
            analogWrite(redPin[i], 0);
        }
    }
}