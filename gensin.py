import math
import sys

SIN_RANGE=256
SCALE=100

sin=[]
for x in range(0,SIN_RANGE):
    sin.append(int(math.sin(math.pi*2/SIN_RANGE*x)*SCALE))

with open("sin.bin", "wb") as f:
    for val in sin:
        lsb=val%256
        msb=val/256
        if lsb<0:
            lsb+=256
        if msb<0:
            msb+=256
        f.write(bytearray([lsb, msb]));
