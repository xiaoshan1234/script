from pathlib import Path
import  sys
import argparse
import subprocess

strCondaConf = \
"""
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  deepmodeling: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
"""

if "__main__" == __name__:
    parser = argparse.ArgumentParser(description='change conda source.')
    parser.add_argument('-s', '--source', type=str, choices=["qs","utsc","aliy"], default='qs', help='qs  or utsc')
    args = parser.parse_args()

    subprocess.run("conda config --set show_channel_urls yes".split(sep=" "))

    fpCondaConf = Path("~/.condarc").expanduser()

    with fpCondaConf.open('w') as fdCondaConf:
        fdCondaConf.write(strCondaConf)

    subprocess.run("conda config --show-sources".split(" "))        

     