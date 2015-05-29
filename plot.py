import matplotlib.pyplot as plt

#plt.plot([1,2,3,4], [1,4,9,16], 'ro')
#plt.axis([0, 6, 0, 20])
#plt.show()
o_list = []

for x in range(0, 100):
    o_list.append(x)

plt.plot(o_list, 'ro')
plt.axis([0, 102, 0, 102])
plt.show()


            #check = ser.read(3)
            #check = int(check,16)
            #print "check if correct", check
            #x=ser.read(2)
            #y=ser.read(2)
            #x = x + ser.read(1)
            #x = int(x,16)
            #y = int(y,16)
            #print "x is: ",x
            #print hex(x)
            #x = hex(x<<5)
            #x = int(x,16)
            #print x
            #print int(x.encode('hex'), 16)
            #print "y is: ", y
            #print "int x: " , int(x)
            #print "int y: " , int(y)
            #myArray = bitarray(32, str(x))
            #x = format(x, '016b')
            #y = format(y, '016b')
            #myArray = bitarray(x)
            #yArray = bitarray(y)
            #print myArray
            #print leftshift(myArray,5)
            #print myArray & 0xF9
            #x = np.left_shift(x,5)
            #x<<5
            #ret_x = np.bitwise_and(x, 0xF9)
            #ret_y = np.bitwise_and(y, 0x1F)
            #ret_x = np.bitwise_and(x, 992)
            #ret_y = np.bitwise_and(y, 31)
            #ret_x = hex(ret_x).rstrip("L").lstrip("0x") or "0"
            #ret_y = hex(ret_y).rstrip("L").lstrip("0x") or "0"
            #print ret_x
            #print ret_y
            #ret = np.bitwise_or(ret_x,ret_y)
            #print "ret: ",ret
            #print ret_x + ret_y
            #print int(y.encode('hex'), 16)
            #if np.bitwise_and(x,0x6) == 0x0:
             #   y = ser.read()
            #ret = bit
             
            #  print x
           # print y
            #test_list.append(x)
            #text_file.write(x)
            #text_file.write(y)
            ##possibly used to determine EOF
            #if x=="\n":
             #    text_file.seek(0)
            # text_file.truncate()