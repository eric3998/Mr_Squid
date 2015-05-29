#Authors: Eric Amzaleg & Jeffrey Franco 
#Desciption: Python program that is used to retrive data from 
#            an Ardiuno board that is then written onto a text file
#            to be used for research.  

## import the serial library
import serial
import array
import struct 
import binascii
import time
import numpy as np
from bitarray import bitarray
import matplotlib.pyplot as plt

def leftshift(ba, count):
    return ba[count:] + (bitarray('0') * count)

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
test_list =  [0]

o_list = []

## read serial data from arduino and 
## write it to the text file 'test_output.txt'
def readFirst(ser):
    x=ser.read(2)
    y=ser.read(2)
    x = int(x,16)
    y = int(y,16)
    print "x is: ",x
    x = hex(x<<5)
    x = int(x,16)
    #print x
    #print int(x.encode('hex'), 16)
    print "y is: ", y
    ret_x = np.bitwise_and(x, 992)
    ret_y = np.bitwise_and(y, 31)
    print ret_x
    print ret_y
    ret = np.bitwise_or(ret_x,ret_y)
    print "ret: ",ret
    ret

def read(ser, x):
    #x=ser.read(2)
    x = x + ser.read(1)
    y=ser.read(2)
    x = int(x,16)
    y = int(y,16)
    print "x is: ",x
    x = hex(x<<5)
    x = int(x,16)
    #print x
    #print int(x.encode('hex'), 16)
    print "y is: ", y
    ret_x = np.bitwise_and(x, 992)
    ret_y = np.bitwise_and(y, 31)
    print ret_x
    print ret_y
    ret = np.bitwise_or(ret_x,ret_y)
    print "ret: ",ret
    ret


count = 0
while count < 1028:
    if ser.inWaiting():
        temp = ser.read()
        if temp == 'a':
            test_list.append(readFirst(ser))
            while count < 1027:
                nxt = ser.read()
                if nxt == 'a':
                    test_list.append(readFirst(ser))
                else:
                    test_list.append(read(ser,nxt))
                count = count + 1
        count = count + 1


##
#  This is where I am trying to figure out how to use 
#  matplotlib      

#for x in range(0, len(test_list)-1):
    #o_list.append(x)

plt.plot(test_list)
plt.axis([0, 400, 0, 400])
plt.show()

#Packing the data recieved 
#packed_data = struct.pack('%sc' % len(test_list), *test_list)

#print 'Original values:', test_list
#print 'Packed Value   :', binascii.hexlify(packed_data)

##unpack to test the ouput
#unpacked_data = struct.unpack('%sc' % len(test_list), test_list)
#print 'Unpacked Values:', unpacked_data

#raw = np.uint64(unpack(fmt,reply))

## close the serial connection and text file
text_file.write("\n*******End of new Test*********\n")
text_file.close()
ser.close()
