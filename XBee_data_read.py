from digi.xbee.devices import XBeeDevice,RemoteXBeeDevice,XBee64BitAddress
import numpy
import serial
i=1;

local_xbee=XBeeDevice("/dev/ttyUSB0",9600)
local_xbee.open()

remote_xbee=RemoteXBeeDevice(local_xbee,XBee64BitAddress.from_hex_string("0013A200415656E8"))


while i<=100:
    
    db=local_xbee.get_parameter("DB")
    file=open("/home/pi/test1.xlt","a")
    x=db;
    file.write("%s\n"%x[0])
    i+=1
    print("%s\n"%x[0])
    remote_xbee.read_device_info(
