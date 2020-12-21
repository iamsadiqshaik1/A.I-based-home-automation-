#include<Stepper.h>
#define steps 32

Stepper stepper(steps,7,8,9,10);
int val=0;
int datauser=0;
int led1=13;
int led2=12;
int led3=11;

void setup() {
  // put your setup code here, to run once:
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
   pinMode(led3,OUTPUT);
  Serial.begin(9600);
  stepper.setSpeed(200);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0)
  {
    datauser=Serial.read();
    
  }
  if(datauser=='1')
  {
    digitalWrite(led1,HIGH);
  }
  else if(datauser=='2')
  {
    digitalWrite(led2,HIGH); 
  }
              
  else if(datauser=='3')
  {
    digitalWrite(led3,HIGH);
    
  }
  else if(datauser=='4')
  {
    digitalWrite(led1,LOW);
  }
    else if(datauser=='5')
    digitalWrite(led2,LOW);
    else if(datauser=='6')
    {
    digitalWrite(led3,LOW);
  }
  else if(datauser=='7')
  {
   digitalWrite(led3,HIGH);
   digitalWrite(led2,HIGH);
   digitalWrite(led1,HIGH); 
  }
  else if(datauser=='0')
  {
    digitalWrite(led3,LOW);
    digitalWrite(led2,LOW);
    digitalWrite(led1,LOW);
 
  }
  else if(datauser=='9')
  {
    val=2000;
    stepper.step(val);
    Serial.println(val);
  }
  }
