import os
"""
需要root权限，若无root权限，添加的库会到用户目录下，不处于PATH里
若添加包失败，
1.尝试包是否是python内置的包
2.查看包的名字是否正确，特别是 “-”与“_”
"""
#web tools
"""
requests,django,bs4,chardet,fake_useragent
"""

#data tools
"""
numpy,pandas,matplotlib,
"""

#AI tools
"""
opencv-python,tensorflow==2.6.0
"""

#os tools
"""

"""

myEnv = "windows"
mylib_str = "requests,django,bs4,chardet,fake_useragent,numpy,pandas,matplotlib,"

if(myEnv == "ubuntu"):
    mylib_str = mylib_str.replace("\n","")#去除回车
    mylib_list = mylib_str.split(",")
    for one in mylib_list:
        os.system("sudo pip3 install "+ one)

elif myEnv == "windows":
    mylib_str = mylib_str.replace("\n","")#去除回车
    mylib_list = mylib_str.split(",")
    for one in mylib_list:
        os.system("powershell pip install "+ one)
else:
    print("系统环境未选择！")

