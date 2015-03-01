#define FASTADC 0
//#include <KeyboardController.h>

// defines for setting and clearing register bits
#ifndef cbi
#define cbi(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif
#ifndef sbi
#define sbi(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

void setup(){

   //extern unsigned int buffer[1024];
   #if FASTADC
    ///set prescale to 16
    sbi(ADCSRA,ADPS2) ;
    cbi(ADCSRA,ADPS1) ;
    cbi(ADCSRA,ADPS0) ;
   #endif
    
   Serial.begin(9600) ;

}

void loop(){
  //Serial.println("Going into loop");
  //Serial.flush();
  read();
  delay(1000);
}

void read(){
  int j = 0 ;
  int buffer[128];
  //Serial.println("Starting the Read loop");
  for(j=0 ; j < 128; j++){
    buffer[j] = (analogRead(0));
    delayMicroseconds(100000);
  }
  
  //Serial.println("Printing out buffer: ");
  for(j=0 ; j<128; j++){
   int temp = buffer[j];
   char upper = (((temp >> 5) & 0x00FF));
   char lower = (buffer[j] & 0x001F);
   
   upper >> 3;
   lower >> 3;
   
   
   if(j == 0){
     
     upper |= 0x0060;
     lower |= 0x0040;
   }
   else{
     upper |= 0x20;
     lower |= 0x00;
   }

   //Serial.print("upper: ");
   //if(j==0)
     //Serial.print();
   Serial.print(upper);
   //Serial.print(" lower: "); 
   Serial.print(lower);
   //Serial.println();
   //}
   //Stuct.unpack 
   //struct.pack
  }
 
 //Serial.flush();
}

