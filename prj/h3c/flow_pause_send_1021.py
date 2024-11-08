from scapy.all import *
from scapy.fields import *
import time
import random

# 定义以太网 Pause 帧
pause_frame = Ether(
    dst="01:80:C2:00:00:01",  # 泛洪地址，用于流控暂停帧
    src="F4:84:8D:8A:0C:5C",  # 发送方 MAC 地址，例如：00:11:22:33:44:55
    type=0x8808  # 表示以太网控制帧
) / Raw(
    load="\x00\x01\xff\x79\x00\x00"  # 控制帧中的Pause Opcode和暂停时间
)

while True:
    for i in range(15):
        sendp(pause_frame, iface="以太网")
    

    