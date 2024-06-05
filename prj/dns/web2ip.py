import socket
from pprint import pprint

# IN  host, port, family, socktype, proto, flags
# OUT family, socktype, proto, canonname, sockaddr
infolist = socket.getaddrinfo("localhost",80)
pprint(infolist)
print("********************************************************")
infolist = socket.getaddrinfo("www.baidu.com",443,family=socket.AF_INET6)
pprint(infolist)
print("********************************************************")
infolist = socket.getaddrinfo(host=None,port=443,family=socket.AF_INET)
pprint(infolist)
