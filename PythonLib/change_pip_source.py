import os
myEnv = "windows"
source = \
"""
[global]
trusted-host = mirrors.aliyun.com
index-url = http://mirrors.aliyun.com/pypi/simple/
"""
myEnv = input("linux or windows ?\n")
if(myEnv == "linux"):
    pipPath = os.path.expanduser("~/.pip/")
    if(not os.path.exists(pipPath)):
        os.mkdir(pipPath)
    with open(pipPath+"pip.conf","w") as myfile:
        myfile.write(source)      
elif(myEnv == "windows"):
    pipPath = os.path.expanduser("~/pip/")
    if(not os.path.exists(pipPath)):
        os.mkdir(pipPath)
    with open(pipPath+"pip.ini","w") as myfile:
        myfile.write(source)  
"""
清华：https://pypi.tuna.tsinghua.edu.cn/simple
阿里云：http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
华中理工大学：http://pypi.hustunique.com/
山东理工大学：http://pypi.sdutlinux.org/
豆瓣：http://pypi.douban.com/simple/
"""   