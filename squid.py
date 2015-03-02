#Authors: Eric Amzaleg & Jeffrey Fraco 
#Desciption: Python program that is used to retrive data from 
#            an Ardiuno board that is then written onto a text file
#            to be used for reasearch.  

## import the serial library
import serial
import array
import struct 
import binascii
import time

## Boolean variable that will represent 
## whether or not the arduino is connected
connected = False

## establish connection to the serial port that your arduino 
## is connected to.
locations=['/dev/tty.usbmodem1411','COM4']

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
##data received from the SQUID    
text_file = open("test_output.txt", 'a')
text_file.write("\n\nStart of new Test: ")
text_file.write(time.ctime())
text_file.write('\n')

#list used to store the read characters
test_list =  []

## read serial data from arduino and 
## write it to the text file 'test_output.txt'
count = 0
while count < 1028:
    if ser.inWaiting():
        x=ser.read()
        print x
        test_list.append(x)
        text_file.write(x)
        ##possibly used to determine EOF
        #if x=="\n":
         #    text_file.seek(0)
         # text_file.truncate()
        count = count + 1

#Packing the data recieved 
packed_data = struct.pack('%sc' % len(test_list), *test_list)

print 'Original values:', test_list
print 'Packed Value   :', binascii.hexlify(packed_data)

##unpack to test the ouput
#unpacked_data = struct.unpack('%sc' % len(test_list), packed_data)
#print 'Unpacked Values:', unpacked_data

## close the serial connection and text file
text_file.write("\n*******End of new Test*********\n")
text_file.close()
ser.close()
