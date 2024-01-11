import argparse
import subprocess
from debug_tool import *
import base64

myArgParser = argparse.ArgumentParser(description = """a transformer bettween base64 and hex""")

myArgParser.add_argument("mode", 
                         type = str, 
                         choices = ["b2a","a2b"],
                         help = "b2a: base64 to hex, a2b: hex to base64")

myArgParser.add_argument("--data", 
                         type = str, 
                         help = "Input Data ")

myArgs = myArgParser.parse_args()


if "__main__" == __name__ :
    strSrcData = ""
    if(myArgs.data):
        strSrcData = myArgs.data
    else:
        strSrcData = input()

    debug_eprint("len {0}".format(len(strSrcData)))
    debug_print("src:", strSrcData)
    if("a2b" == myArgs.mode):
        # encodestring 会加个 \n
        print(str(base64.encodestring(strSrcData.encode())[:-1], "utf-8"))
    elif("b2a" == myArgs.mode):
        print(str(base64.decodestring(strSrcData.encode()), "utf-8"))

