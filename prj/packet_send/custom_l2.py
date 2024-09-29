from scapy.all import *
from scapy.fields import *

# 定义自定义协议类
class MyLayer(Packet):
    name = "MyLayer"
    fields_desc = [
        XShortField("field1", 0x1234),  # 2字节字段
        IntField("field2", 0),          # 4字节字段
        StrFixedLenField("field3", "data", length=4)  # 固定长度字符串
    ]

# 注册自定义协议
bind_layers(Ether, MyLayer, type=0x88B5)  # 使用一个假设的以太网类型

# 创建带有自定义协议的二层报文
packet = Ether(dst="ff:ff:ff:ff:ff:ff") / MyLayer(field1=0x5678, field2=42, field3="test")

# 显示数据包细节
packet.show()

# 发送数据包
sendp(packet, iface="eth0")