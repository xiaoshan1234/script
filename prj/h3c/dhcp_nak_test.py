from scapy.all import *
import random
import binascii
# 指定网卡名称
iface_name = "以太网"

nakCount = 0
localIP = "192.168.28.28"
localMac = "F4:84:8D:8A:0C:5C"

def generate_random_ip():
    return "%03d.%03d.%d.%d" % (
        192,
        168,
        28,
        random.randint(30, 250)
    )


def get_dhcp_nak(packet, reqaddr, chaddr, xid):
    # 目标 MAC 地址 (这里填写实际客户端 MAC 地址)
    client_mac = chaddr

    # 使用 binascii 将字符串转换为字节
    chaddr_bytes = binascii.unhexlify(client_mac.replace(':', ''))

    # 确保 chaddr 字节长度为 16
    chaddr = chaddr_bytes + b'\x00' * (16 - len(chaddr_bytes))

    # 构建 Ethernet 层
    ethernet = Ether(dst=client_mac, src=localMac, type=0x0800)
    
    # 构建 IP 层
    ip = IP(src=localIP, dst="255.255.255.255")  # 通常目标IP为广播地址
    
    # 构建 UDP 层
    udp = UDP(sport=67, dport=68)
    
    # 构建 BOOTP 层
    bootp = BOOTP(
        op=2,  # 2表示回复包
        xid=xid,  # 事务 ID (需要与请求匹配)
        chaddr=chaddr,
        flags=0
    )
    
    # 构建 DHCP 层
    dhcp = DHCP(
        options=[
            ("message-type", "nak"),
            ("server_id", localIP),
            "end"
        ]
    )

    # 构建完整的数据包
    packet = ethernet / ip / udp / bootp / dhcp

    return packet


def get_dhcp_ack(packet, reqaddr, chaddr, xid):
    # 目标 MAC 地址 (这里填写实际客户端 MAC 地址)
    client_mac = chaddr

    # 构建 Ethernet 层
    ethernet = Ether(dst=client_mac, src=localMac, type=0x0800)
    
    # 构建 IP 层
    ip = IP(src=localIP, dst=reqaddr)  # 这里填写实际 DHCP 服务器和客户端 IP 地址
    
    # 构建 UDP 层
    udp = UDP(sport=67, dport=68)
    
    # 构建 BOOTP 层
    bootp = BOOTP(
        op=2,  # 2表示回复包
        yiaddr=reqaddr,  # 客户端被分配的 IP 地址
        siaddr=localIP,  # DHCP 服务器的 IP 地址
        chaddr=client_mac.replace(':', '').decode('hex') + b'\x00' * 10,
        xid=xid,  # 事务 ID (需要与请求匹配)
        flags=0
    )
    
    # 构建 DHCP 层
    dhcp = DHCP(
        options=[
            ("message-type", "ack"),
            ("server_id", localIP),
            ("lease_time", 43200),  # 租约时间
            ("subnet_mask", "255.255.255.0"),
            ("router", localIP),
            ("name_server", "8.8.8.8"),
            "end"
        ]
    )

    # 构建完整的数据包
    packet = ethernet / ip / udp / bootp / dhcp

    return packet


def get_dhcp_offer(packet, yiaddr, chaddr, xid):
    # Ethernet layer
    ether = Ether(dst="ff:ff:ff:ff:ff:ff", src=localMac, type=0x0800)

    # IP layer
    ip = IP(src=localIP, dst="255.255.255.255")

    # UDP layer
    udp = UDP(sport=67, dport=68)

    # BootP layer
    bootp = BOOTP(
        op=2,  # BOOTREPLY
        yiaddr=yiaddr,  # The IP being offered to the client
        siaddr=localIP,  # Server IP
        chaddr=chaddr,  # Client MAC address
        xid=xid  # Transaction ID
    )

    # DHCP layer
    dhcp = DHCP(
        options=[
            ('message-type', 'offer'),  # DHCP Offer
            ('server_id', localIP),  # DHCP server identifier
            ('lease_time', 3600),  # Lease Time
            ('subnet_mask', '255.255.255.0'),  # Subnet Mask
            ('router', localIP),  # Router
            ('end')
        ]
    )

    # Create the full packet
    dhcp_offer = ether / ip / udp / bootp / dhcp
    
    return dhcp_offer


def handle_dhcp_discover(packet):
    print("DHCP Discover Packet Received:")
    packet.show()    
    bootp_layer = packet[BOOTP]
    yiaddr = generate_random_ip()
    chaddr = ":".join(["%02x" % b for b in bootp_layer.chaddr[:6]])  # 取前6字节为MAC地址
    xid = bootp_layer.xid
    dhcp_offer_packet = get_dhcp_offer(packet, yiaddr, chaddr, xid)
    sendp(dhcp_offer_packet, iface=iface_name, verbose=1)
    print("DHCP Offer Packet Send:")
    dhcp_offer_packet.show()


def handle_dhcp_request(packet): 
    print("DHCP Request Packet Received:") 
    packet.show() 
    bootp_layer = packet[BOOTP]  
    # yiaddr = bootp_layer.yiaddr
    chaddr = ":".join(["%02x" % b for b in bootp_layer.chaddr[:6]])  # 取前6字节为MAC地址
    xid = bootp_layer.xid
    requested_ip = ""
    dhcp_options = packet[DHCP].options
    for opt in dhcp_options:
        if opt[0] == 'requested_addr':
            requested_ip = opt[1]
            print(f"Requested IP: {requested_ip}")
            break    
    if True:
        # nakCount = nakCount+1
        dhcp_ack_packet = get_dhcp_nak(packet, requested_ip, chaddr, xid)
        print("DHCP Nak Packet Send:")
    else:
        dhcp_ack_packet = get_dhcp_ack(packet, requested_ip, chaddr, xid)
        print("DHCP Ack Packet Send:")
    sendp(dhcp_ack_packet, iface=iface_name, verbose=1)
    dhcp_ack_packet.show()        

    
# DHCP 数据包的回调函数
def handle_dhcp_packet(packet):
    # 检查数据包是否包含 DHCP 层
    if packet.haslayer(DHCP):
        # 遍历 DHCP 选项以找到消息类型
        dhcp_options = packet[DHCP].options
        for option in dhcp_options:
            if option[0] == 'message-type':
                dhcp_message_type = option[1]
                # 打印根据发现的 DHCP 消息类型
                if dhcp_message_type == 1:  # DHCP Discover
                    handle_dhcp_discover(packet)
                elif dhcp_message_type == 3:  # DHCP Request
                    handle_dhcp_request(packet)
                break  # 找到 DHCP 消息类型就可以退出循环

# 监听端口67上的DHCP数据包
def listen_dhcp():
    # 使用scapy的sniff方法来捕获数据包
    sniff(
        # filter="udp and (port 67 or port 68)",  # 过滤DHCP请求 (68) 和回应 (67)
        filter="udp and port 68",
        prn=handle_dhcp_packet,  # 每个包解析的回调方法
        store=0,  # 不存储包在内存中
        iface=iface_name  # 替换为你的网络接口
    )

# 开始监听
if __name__ == '__main__':
    listen_dhcp()