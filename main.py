#from converter import * 

f = 1.23
data = Converter.floatToBytes(False, f)

print(data)

datain = [0x3f, 0x80, 0xab, 0xcd]

f = Converter.bytesToFloat(True, datain)

x = 0x3f800000

y = x & 0x00ff0000

print(y)
