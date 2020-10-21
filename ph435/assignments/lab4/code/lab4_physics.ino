/*
Lab 4
Ping-Pong with physics
*/

// used pins
#define leftPlayer 2
#define rightPlayer 3
#define playerPin(x) (x + 5)
  // LED outputs
int redPin[4] = {5, 9, 10, 11}; // pins grouped by the same frequency
int grePin[2] = {7, 8}; // use playerPin(x) macro instead for compile time resolution


// variables
#define maxWait 500
uint8_t state = 0; // start state
uint8_t ball[2] = {0, 1}; // position 0, moving right
uint8_t ballInRange = 0; // 0 = none, 1 = left, 2 = right
volatile bool leftHit = false, rightHit = false;
bool lightOn = 0;
uint16_t lightOnStart = 0;
unsigned long ballWait = 0; // time ball has been near player
uint8_t victory = 0; // has a player won? if yes, which?

// functions
void leftPlayerHit();
void rightPlayerHit();
void changeOutputs();

void setup(){
    Serial.begin(1000000); // why not
    DDRD |= 0b11111110; // pins 1-7 as output. 0 is Tx
    DDRB |= 0x11111111; // set all pins 8-13 (and dummy bits) to output
    PORTD = 0x0;  // initialise as low 
    PORTB = 0x0;

    changeOutputs(); // initial lights
    pinMode(leftPlayer, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(leftPlayer), leftPlayerHit, FALLING);
    pinMode(rightPlayer, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(rightPlayer), rightPlayerHit, FALLING);
}

void loop(){

    if(lightOn){
      if((millis() - lightOnStart) >= maxWait){
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


    // delay(100); // delay to control clock speed

    switch (state)
    {
    case 0:
      // initial state
      // wait for first input
      if(leftHit) {state = 1; leftHit = 0;}
      break;

    case 1:
      // game in play
      if(ball[0] <= 0 && ball[0] >= 3){
        // somewhere in the middle
        ball[0] += ball[1]; // x = x + v.dt
        changeOutputs();
        break;
      }
      else{
        ballInRange = (ball[0] <= 0) ? 1 : -1;
        ball[0] = (ball[0] <= 0) ? 0 : 3; // bring ball back in range
        // start counter
        ballWait = millis();
      }
    
    case 2:
      // ball in left range
      if(ballWait >= maxWait){
        victory = rightPlayer;
        state = 4;
        break;
      }
      if(!leftHit) break;

      ball[1] = (ballWait > 250) ? 2 : 1; // travel to right
      leftHit = false; // reset
      digitalWrite(playerPin(leftPlayer), 1); // light up
      lightOn = true; lightOnStart = millis();
      state = 1;
      break;
    
    case 3:
      // ball in right range
      if(ballWait >= maxWait){
        victory = rightPlayer;
        state = 4;
        break;
      }
      if(!leftHit) break;

      ball[1] = -1; // travel to left
      rightHit = false; // reset
      digitalWrite(playerPin(rightPlayer), 1); // light up
      lightOn = true; lightOnStart = millis();
      state = 1;
      break;
    
    case 4:
      // ball miss
      // flash 4 times;
      for(int i = 1; i <= 8; i++){
        digitalWrite(victory, i%2);
        delay(500);
      }
      // go back to initial
      ball[0] = 0;
      ball[1] = 1;
      ballInRange = 0;
      state = 0;
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

  if(ballInRange = 1){
    leftHit = true;
  }

  return;
}

void rightPlayerHit(){

  if(ballInRange == -1){
    rightHit = true;
  }

  return;
}

void changeOutputs(){
    int dir = (ball[1] > 0);
    for(int i = 0; i < 4; i++){
        if((ball[0] == i) || (ball[0] == (i - dir))){
            // leave a trail
            analogWrite(redPin[i], 127 + 128 * ((int) (ball[0] == i)));
        }
        else{
            analogWrite(redPin[i], 0);
        }
    }
}