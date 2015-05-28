#!/usr/bin/env python2.5

#import Gnuplot
import serial
import sys

ser = serial.Serial(sys.argv[1], 9600)

readings = []
#g = Gnuplot.Gnuplot()
#g.title("Thermistor readings")
#g('set data style lines')
#g('set yrange [-5:105]')

while 1:
   reading = ser.readline().split()
   print reading

   readings.append(reading)

   if len(readings) > 100:
       readings = readings[-10:]

   #g.plot(readings)