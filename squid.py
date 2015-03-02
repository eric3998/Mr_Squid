## import the serial library
import serial
import array
import struct 
import binascii

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

test_list =  []
## read serial data from arduino and 
## write it to the text file 'position.txt'
count = 0
while count < 10:
    if ser.inWaiting():
        x=ser.read()
        print x
        test_list.append(x)
        text_file.write(x)
        #if x=="\n":
         #    text_file.seek(0)
         # text_file.truncate()
        count = count + 1

#s = struct
packed_data = struct.pack('%sc' % len(test_list), *test_list)

print 'Original values:', test_list
#print 'Format string  :', s.format
#print 'Uses           :', s.size, 'bytes'
print 'Packed Value   :', binascii.hexlify(packed_data)
#unpacked_data = struct.unpack('%sc' % len(test_list), packed_data)
#print 'Unpacked Values:', unpacked_data

## close the serial connection and text file
text_file.close()
ser.close()