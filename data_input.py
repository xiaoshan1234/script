import numpy as np
import pandas as pd
import re
import argparse
import subprocess
from debug_tool import *

myArgParser = argparse.ArgumentParser(description = "")

myArgParser.add_argument("type", 
                         type = str, 
                         choices = ["hex",],
                         help = "Data Format")

myArgParser.add_argument("--data", 
                         type = str, 
                         help = "Input Data ")

myArgs = myArgParser.parse_args()

def ascii2hex(strAcsii:str):
    debug_print("a2h: ",end="")
    for i in range(len(strAcsii)):
        print("{0:x}".format(ord(strAcsii[i])), end="")

ptnSp = re.compile(r"\w{2}")

                
if "__main__" == __name__ :
    strSrcData = ""
    if(myArgs.data):
        strSrcData = myArgs.data
    else:
        strSrcData = input()

    debug_print("src:", strSrcData)
    if("hex" == myArgs.mode):
        ascii2hex(strSrcData)





