from scapy.all import *
from scapy.contrib.lldp import LLDPDU, LLDPDUChassisID, LLDPDUPortID, LLDPDUTimeToLive

# 构建LLDP数据包
lldp_packet = Ether(dst="01:80:c2:00:00:0e") / (
    LLDPDU() /
    LLDPDUChassisID(subtype=4, id="00:11:22:33:44:55") /
    LLDPDUPortID(subtype=5, id="eth0") /
    LLDPDUTimeToLive(ttl=120)
)

# 发送LLDP数据包
for i in range(10):
    sendp(lldp_packet, iface="以太网", verbose=True)