import os
"""
需要root权限，若无root权限，添加的库会到用户目录下，不处于PATH里
若添加包失败，尝试包是否是python内置的包
"""

"""
numpy,
requests,
django,
json,
bs4,
pandas,
matplotlib,
opencv
"""

myEnv = "linux"
mylib_str = "opencv-python"

print("the current py env is:")
os.system("conda info -e")



'''
1 change anaconda source
2 update anaconda
3 anser yes
'''
os.system("conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/")
os.system("conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge")
os.system("conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/")
os.system("conda config --set show_channel_urls yes")

if(myEnv == "linux"):
    mylib_str = mylib_str.replace("\n","")#去除回车
    mylib_list = mylib_str.split(",")
    for one in mylib_list:
        os.system("sudo pip3 install "+ one)
elif myEnv == "windows":
    mylib_str = mylib_str.replace("\n","")#去除回车
    mylib_list = mylib_str.split(",")
    for one in mylib_list:
        os.system("powershell pip install "+ one)
