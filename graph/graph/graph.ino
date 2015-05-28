#define REPORTING_INTERVAL 1

float time;
int reading;

void read_pin(char pin)
{
   while (1) {
       time = 0.001 * millis();
       reading = analogRead(pin);
       Serial.print(time);
       Serial.print(' ');
       Serial.println(reading);
       delay(1000*REPORTING_INTERVAL);
   }
}

void setup()
{
   Serial.begin(9600);
   delay(100);
}


void loop()
{
   read_pin(0);
}
