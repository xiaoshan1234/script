import argparse
import subprocess
from debug_tool import *

myArgParser = argparse.ArgumentParser(description = """a transformer bettween ascii and hex""")

myArgParser.add_argument("mode", 
                         type = str, 
                         choices = ["a2h","h2a"],
                         help = "a2h: ascii to hex, h2a: hex to ascii")

myArgParser.add_argument("--data", 
                         type = str, 
                         help = "Input Data ")



myArgs = myArgParser.parse_args()

def ascii2hex(strAcsii:str):
    debug_print("a2h: ",end="")
    for i in range(len(strAcsii)):
        print("{0:x}".format(ord(strAcsii[i])), end="")


def hex2ascii(strHex:str):
    debug_print("h2a: ",end="")
    if(0 == len(strHex)%2):
        for i in range(0,len(strHex),2):
            print(chr(int(strHex[i:i+2],16)), end="")
    else:
        print("error len {0}".format(len(strHex)))
    


if "__main__" == __name__ :
    strSrcData = ""
    if(myArgs.data):
        strSrcData = myArgs.data
    else:
        strSrcData = input()

    debug_print("src:", strSrcData)
    if("a2h" == myArgs.mode):
        ascii2hex(strSrcData)
    elif("h2a" == myArgs.mode):
        hex2ascii(strSrcData)

