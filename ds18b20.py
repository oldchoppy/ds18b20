import machine,onewire
from machine import Pin
from onewire import OneWire
import time

class ds:
    def __init__(self, pin=2, unit='c', resolution=12):
        self.pin=pin
        self.addr=None
        self.unit=unit
        self.res=resolution
        self.getaddr()
    def getaddr(self):
        ow=OneWire(Pin(self.pin))
        a=ow.scan()
        self.addr=a[0]

def _res(self):
    ow=OneWire(Pin(self.pin))
    ow.reset()
    ow.select_rom(self.addr)
    ow.writebyte(0x4E)
    if self.res==12:
        ow.writebyte(0x7F)
        ow.writebyte(0x7F)
        ow.writebyte(0x7F)
        print ("12 bit mode")
    if self.res==11:
        ow.writebyte(0x5F)
        ow.writebyte(0x5F)
        ow.writebyte(0x5F)
        print ("11 bit mode")
    if self.res==10:
        ow.writebyte(0x3F)
        ow.writebyte(0x3F)
        ow.writebyte(0x3F)
        print ("10 bit mode")
    if self.res==9:
        ow.writebyte(0x1F)
        ow.writebyte(0x1F)
        ow.writebyte(0x1F)
        print ("9 bit mode")
    ow.reset()

def read(self):
    _res(self)
    ow=OneWire(Pin(self.pin))
    ow.reset()
    ow.select_rom(self.addr)
    ow.writebyte(0x44)
    time.sleep(1)
    ow.reset()
    ow.select_rom(self.addr)
    ow.writebyte(0xBE)
    LSB=ow.readbyte()
    MSB=ow.readbyte()
    ow.readbyte()
    ow.readbyte()
    print (bin(ow.readbyte()))
    ow.readbyte()
    ow.readbyte()
    ow.readbyte()
    ow.readbyte()
    ow.reset()
    d_LSB=float(0)
    d_MSB=float(0)
    count=0
    b=bin(LSB)
    b2=bin(MSB)
    b3=""
    l=10-len(b2)
    for i in range(l):
        if len(b2)<10:
            b3+="0"
    b2=b3+b2
    b4=""
    l=10-len(b)
    for i in range(l):
        if len(b)<10:
            b4+="0"
    b5=b4+b
##    print ("LSB: "+str(b))
##    print("converted binary for LSB: "+str(b5))
##    print ("MSB: "+str(b2))
    for i in b5:
        if count == 2:
            if i=='1':
                d_LSB+=2**3
        if count == 3:
            if i=='1':
                d_LSB+=2**2
        if count == 4:
            if i=='1':
                d_LSB+=2**1
        if count == 5:
            if i=='1':
                d_LSB+=2**0
        if count == 6:
            if i=='1':
                d_LSB+=2**-1
        if count == 7:
            if i=='1':
                d_LSB+=2**-2
        if count == 8:
            if i=='1':
                d_LSB+=2**-3
        if count == 9:
            if i=='1':
                d_LSB+=2**-4
        count+=1
    count=0
    sign=1
##    print("converted binary for MSB: "+str(b2))
    for i in b2:
        if count == 6:
            if i=='1':
                sign=-1
        if count == 7:
            if i=='1':
                d_MSB+=2**6
        if count == 8:
            if i=='1':
                d_MSB+=2**5
        if count == 9:
            if i=='1':
                d_MSB+=2**4
        count+=1
    temp=(d_LSB+d_MSB)*sign
    if self.unit=='c'or self.unit=='C':
        print("TEMP is: "+str(temp)+" degrees C")
    if self.unit=='f'or self.unit=='F':
        temp=(temp*9/5)+32
        print("TEMP F is: "+str(temp))
    return temp



