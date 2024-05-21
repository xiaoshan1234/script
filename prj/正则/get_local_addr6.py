from pathlib import Path
import  sys
import subprocess as sp
import re


if "__main__" == __name__:
    if sys.platform.startswith('win'):
        cmdList = ["ipconfig"]
        ptnGlbIPv6 = re.compile(r"\n\s+IPv6 地址[\. \s]+:\s+(2[a-f0-9:]*)")
    elif sys.platform.startswith('lin'):
        cmdList = ["ip","a"]
        ptnGlbIPv6 = re.compile(r"inet6\s*(2[a-f0-9:]*)/")

    objCmpltProcess = sp.run(cmdList,capture_output=True,encoding="gb2312")
    rstSearch = ptnGlbIPv6.search(objCmpltProcess.stdout) 
    print(rstSearch.group(1))
    