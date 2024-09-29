from scapy.all import *
from scapy.fields import *

# 发现
class UsmpDiscover(Packet):
    name = "UsmpDiscover"
    fields_desc = [
        XShortField("Type1", 0x0003),  # 2字节字段，固定 3
        ShortField("Lenth1", 0x000),  # 2字节字段，TLV的总长度 T + L + V
        StrFixedLenField("Reserve1", b"\0"*4, length=4),  # 4字节字段
        MACField("LocalMac", "00:11:22:33:44:55"),  # 固定长度字符串
        StrFixedLenField("Reserve2", b"\0"*2, length=2),  # 2字节字段
        IPField("TmManageIP", "127.0.0.1"),
        IPField("TmManageIPMask", "255.0.0.0"),
        StrFixedLenField("HostName", b"\0"*65, length=65),
        StrFixedLenField("Reserve3", b"\0"*3, length=3),
        IntField("MapCap",0),
        StrFixedLenField("NetId", b"\0"*128, length=128),
        IntField("DevPri",0x0),
        IntField("DevHealth",0x0),
        IntField("NetScale",0x0),
        IntField("ScanInterval",0x0),
        IntField("KeepAlivePeriod",0x0),
        ByteField("Upgrading",0x0),
        IntField("BasicCap",0x0),
        IntField("ServiceCap",0x0),
        ByteField("Reserve4",0x0),
        XShortField("Type2", 0x0000), # Type=0 代表 TC状态
        ShortField("Lenth2", 0x0000),
        XStrFixedLenField("TcList", b"\0"*129, length=129),
        XShortField("Type3", 0x0001), # Type=1 代表 管理Vlan
        ShortField("Lenth3", 0x0006),
        ShortField("ManageVlan", 0x0001)        
    ]


# 注册自定义协议
bind_layers(Ether, UsmpDiscover, type=0xabb0)  # 使用一个假设的以太网类型


packets = rdpcap(r'prj\usmp\usmp.pcapng')

for packet in packets:
    if packet.haslayer(UsmpDiscover) and packet[Ether].dst == 'ff:ff:ff:ff:ff:ff':
        print("UsmpDiscover Packet Found:")
        packet.show()
