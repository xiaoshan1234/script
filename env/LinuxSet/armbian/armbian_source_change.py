import os
import time
armbian_aliyun_source = \
"""
deb http://mirrors.ustc.edu.cn/debian stretch main contrib non-free
deb http://mirrors.ustc.edu.cn/debian stretch-updates main contrib non-free
deb http://mirrors.ustc.edu.cn/debian stretch-backports main contrib non-free
deb http://mirrors.ustc.edu.cn/debian-security/ stretch/updates main contrib non-free
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
        myfile.write(armbian_aliyun_source)
else:
    print("conf_file does not exsit")  
    
os.system("apt update")
os.system("apt upgrade")  