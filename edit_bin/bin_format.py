
import numpy as np
import pandas as pd
import re
import argparse
import subprocess
from debug_tool import *
from pathlib import Path

myArgParser = argparse.ArgumentParser(description = "")

myArgParser.add_argument("e", 
                         type = int, 
                         help = "base element size")

myArgParser.add_argument("fp", 
                         type = str, 
                         help = "file path ")

myArgs = myArgParser.parse_args()
                
if "__main__" == __name__ :
    intElementSize =  myArgs.e
    strDataFilePath = myArgs.fp
    debug_print(strDataFilePath)
    objDataFilePath = Path(strDataFilePath)

    if(objDataFilePath.exists() and  objDataFilePath.is_file()):
        debug_print("File exists")
        with open(strDataFilePath, 'rb') as objDataFile:
            # arrData = objDataFile.read(1024)
            arrData = objDataFile.read()
            for i in range(0, len(arrData), intElementSize):
                print("{0:3}, ".format(int.from_bytes(arrData[i:i+intElementSize],"big")),end="")
                if((i+1)%10 ==  0):
                    print("")
