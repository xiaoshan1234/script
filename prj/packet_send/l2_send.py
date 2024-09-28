from scapy.all import *

# 创建一个自定义的Ethernet帧
custom_frame = Ether(dst="ff:ff:ff:ff:ff:ff", src="11:22:33:44:55:66") / Raw(load="Hello, this is a custom payload!")

# 发送自定义帧
sendp(custom_frame, iface="Ethernet", verbose=True)