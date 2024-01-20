import os
import time
debian_source = \
"""
deb https://mirrors.aliyun.com/debian/ bullseye main non-free contrib
deb-src https://mirrors.aliyun.com/debian/ bullseye main non-free contrib
deb https://mirrors.aliyun.com/debian-security/ bullseye-security main
deb-src https://mirrors.aliyun.com/debian-security/ bullseye-security main
deb https://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib
deb-src https://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib
deb https://mirrors.aliyun.com/debian/ bullseye-backports main non-free contrib
deb-src https://mirrors.aliyun.com/debian/ bullseye-backports main non-free contrib
"""
cur_time = time.strftime(r"%Y.%m.%d.%H.%M.%S",time.localtime())

conf_file = "/etc/apt/sources.list"
bak_file = "/etc/apt/sources.list.({}).bak".format(cur_time)
if(os.path.exists(conf_file)):
    with open(conf_file,"r") as myfile:
        text = myfile.read()
    with open(bak_file,"w") as myfile:
        myfile.write(text)
    with open(conf_file,"w") as myfile:
        myfile.write(debian_source)
else:
    print("conf_file does not exsit")  
    
os.system("apt update")
os.system("apt upgrade")  