import os
import time
ubuntu_aliyun_source = \
"""
deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
 
deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
 
deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
 
deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
 
deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
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
        myfile.write(ubuntu_aliyun_source)
else:
    print("conf_file does not exsit")  
    
os.system("apt update")
os.system("apt upgrade")  