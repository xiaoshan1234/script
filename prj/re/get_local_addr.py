from pathlib import Path
import  sys
import subprocess as sp
import re


if "__main__" == __name__:
    if sys.platform.startswith('win'):
        cmdList = ["ipconfig"]
        ptnLocalIPv4 = re.compile(r"\n\s+IPv4 地址[\. \s]+:\s+(1[0-9\.]*)") # \n\s+IPv4 地址[\. \s]+:\s+(1[0-9\.]*)
    elif sys.platform.startswith('lin'):
        cmdList = ["ip","a"]
        ptnLocalIPv4 = re.compile(r"inet\s*(1[0-9\.]*)/") # inet 192.168.1.103/24

    objCmpltProcess = sp.run(cmdList,capture_output=True,encoding="gb2312")
    rstSearch = ptnLocalIPv4.findall(objCmpltProcess.stdout) 
    for obj in rstSearch:
        print(obj)
    