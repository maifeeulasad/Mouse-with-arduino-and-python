int potPin1 = 0;
int potPin2 = 1;
int value1;
int value2;

void setup()
{
  Serial.begin(9600);  
}

void loop() 
{
  value1 = analogRead(potPin1);

  
  value2 = analogRead(potPin2);

  Serial.print(value1);
  Serial.print("   ");
  Serial.print(value2);
  Serial.println("");
  delay(1000);
}
