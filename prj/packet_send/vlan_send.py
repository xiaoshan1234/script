from scapy.all import *

# 创建一个带VLAN标签的Ethernet帧
vlan_frame = Ether(dst="ff:ff:ff:ff:ff:ff", src="11:22:33:44:55:66") / \
             Dot1Q(vlan=10) / \
             IP(dst="192.168.1.1") / \
             ICMP() / \
             Raw(load="Hello, VLAN!")

# 发送带VLAN标签的帧
sendp(vlan_frame, iface="Ethernet", verbose=True)