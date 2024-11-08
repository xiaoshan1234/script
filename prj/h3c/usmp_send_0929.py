from scapy.all import *
from scapy.fields import *
import time
import random

def generate_random_mac():
    # 生成随机MAC地址
    return "02:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff)
    )

def generate_random_ip():
    return "%03d.%03d.%d.%d" % (
        192,
        168,
        random.randint(0, 250),
        random.randint(0, 250)
    )

# 发现
class UsmpDiscover(Packet):
    name = "UsmpDiscover"
    fields_desc = [
        XShortField("Type1", 0x0004),  # 2字节字段
        ShortField("Lenth1", 383),  # 2字节字段
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
        IntField("ScanInterval",15000),
        IntField("KeepAlivePeriod",3),
        ByteField("Upgrading",0x0),
        IntField("BasicCap",0x0),
        IntField("ServiceCap",0x0),
        ByteField("Reserve4",0x0),
        XShortField("Type2", 0x0000), 
        ShortField("Lenth2", 0x0000),
        XStrFixedLenField("TcList", b"\0"*129, length=129),
        XShortField("Type3", 0x0001), 
        ShortField("Lenth3", 0x0006),
        ShortField("ManageVlan", 0x0001)        
    ]


# 注册自定义协议
bind_layers(Ether, UsmpDiscover, type=0xabb0, dst="ff:ff:ff:ff:ff:ff")  # 使用一个假设的以太网类型

while True:
    local_mac = generate_random_mac()
    local_ip = generate_random_ip()
    print(local_ip)
    packet = Ether(dst="ff:ff:ff:ff:ff:ff",src=local_mac) / UsmpDiscover(LocalMac=local_mac,
                                                                         TmManageIP=local_ip,
                                                                         TmManageIPMask="255.255.255.0",
                                                                         HostName="usmp测试8811版本",
                                                                        #  Type3 = random.randint(0, 250),
                                                                        #  Lenth3 = random.randint(0, 250),
                                                                         ManageVlan = random.randint(0, 250))
    packet.show()
    sendp(packet, iface="以太网")
    time.sleep(1)
    