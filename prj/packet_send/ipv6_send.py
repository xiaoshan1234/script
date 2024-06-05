import socket
import struct
import scapy

targetMac = struct.pack("6B",0x58,0x11,0x22,0xda,0xba,0xf0)
targetHeader = struct.pack("B",0xff)*6
magicPktBody = targetHeader + targetMac*16
magicPktUnpack = struct.unpack("6B6B90B",magicPktBody)

socketUdp = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
socketUdp.bind(('fe80::c50:b464:e3b9:7b92',67))

i = 10
while i != 0:
    socketUdp.sendto(magicPktBody, ("fe80::24ba:cd16:7515:828", 68))
    i = i-1