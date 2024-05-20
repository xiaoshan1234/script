import socket
import struct
from pprint import pprint

targetMac = struct.pack("6B",0x58,0x11,0x22,0xda,0xba,0xf0)
targetHeader = struct.pack("B",0xff)*6
magicPktBody = targetHeader + targetMac*16
magicPktUnpack = struct.unpack("6B6B90B",magicPktBody)

socketUdp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketUdp.bind(('localhost',8888))
infolist = socket.getaddrinfo("localhost",80)
pprint(infolist)
i = 10
while i != 0:
    socketUdp.sendto(magicPktBody, ("192.168.28.255", 9))
    i = i-1