from converter import * 
from os import system

# clear screen
system('clear')

# set float value - Hex = 0x3F9D70A4
f = 1.23 

# Convert to big endian byte array
data = Converter.floatToBytes(True, f)

print ("Float to Hex")
print ("------------")
print ("Float : {0}".format(f))
print("B.E. bytes : {0:X}{1:X}{2:X}{3:X}".format(data[0],data[1],data[2],data[3]))

# Convert to little endian byte array
data = Converter.floatToBytes(False, f)

print("L.E. bytes : {0:X}{1:X}{2:X}{3:X}".format(data[0],data[1],data[2],data[3]))


# 12.34 in big endian format
datain = [0x41, 0x45, 0x70, 0xA4]


print()
print ("Hex to Float")
print ("------------")
print("B.E. bytes : {0:X}{1:X}{2:X}{3:X}".format(datain[0],datain[1],datain[2],datain[3]))

# convert to big endian data to float
f = Converter.bytesToFloat(True, datain)

print ("B.E. float : {0}".format(f))

# 12.34 in little endian format
datain = [0xA4, 0x70, 0x45, 0x41]

print("L.E. bytes : {0:X}{1:X}{2:X}{3:X}".format(datain[0],datain[1],datain[2],datain[3]))

# convert to big endian data to float
f = Converter.bytesToFloat(False, datain)

print ("L.E. float : {0}".format(f))
