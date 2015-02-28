## import the serial library
import serial
import array
import struct 

## Boolean variable that will represent 
## whether or not the arduino is connected
connected = False

## establish connection to the serial port that your arduino 
## is connected to.

locations=['/dev/tty.usbmodem1411']

for device in locations:
    try:
        print "Trying...",device
        ser = serial.Serial(device, 9600)
        break
    except:
        print "Failed to connect on",device

## loop until the arduino tells us it is ready
while not connected:
    serin = ser.read()
    connected = True

## open text file to store the current 
##gps co-ordinates received from the rover    
text_file = open("position4.txt", 'a')

test_array = array('c')
## read serial data from arduino and 
## write it to the text file 'position.txt'
count = 0
while count < 1028:
    if ser.inWaiting():
        x=ser.read()
        #print x
        struct.pack(x)
        text_file.write(x)
        #if x=="\n":
         #    text_file.seek(0)
         # text_file.truncate()
        count = count + 1



## close the serial connection and text file
text_file.close()
ser.close()