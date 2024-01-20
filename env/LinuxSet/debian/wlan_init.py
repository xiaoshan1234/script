import os
import time
wlan_set_txt = \
"""
auto {if_name}
iface {if_name} inet dhcp
    wpa-ssid {ssid}
    wpa-psk {passwd}
"""
cur_time = time.strftime(r"%Y.%m.%d.%H.%M.%S",time.localtime())
conf_file = "/etc/network/interfaces" #/etc/network/
bak_file = "/etc/network/interfaces({}).bak".format(cur_time)

os.system("ip a")
print("\nrun this script in root(su - root)\n")
if_name = input("input interface name:\n")
ssid = input("input ssid : \n")
passwd = input("input password :\n")

if(os.path.exists(conf_file)):
    with open(conf_file,"r") as myfile:
        text = myfile.read()
    with open(bak_file,"w") as myfile:
        myfile.write(text)
    with open(conf_file,"a") as myfile:
        myfile.write(wlan_set_txt.format(if_name=if_name,ssid=ssid,passwd=passwd))
    os.system("service networking restart")
    print("Done")
else:
    print("conf_file does not exsit")  
    
