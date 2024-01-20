from pathlib import Path
import  sys
import argparse
import subprocess

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

if "__main__" == __name__:

    if sys.platform.startswith('win'):
        strPip = "pip"
    elif sys.platform.startswith('lin'):
        strPip = "pip3"

    print(f"install:  {strPip} install -r requirements.txt ")
    print(f"export: {strPip} freeze >>  requirements.txt ")
                                
                        









