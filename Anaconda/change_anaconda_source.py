import os
"""
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/

conda config --add channels http://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --add channels http://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels http://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels http://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
conda config --add channels http://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
conda config --add channels http://mirrors.ustc.edu.cn/anaconda/cloud/menpo/
"""

os.system("conda config --add channels http://mirrors.ustc.edu.cn/anaconda/pkgs/main/")
os.system("conda config --add channels http://mirrors.ustc.edu.cn/anaconda/pkgs/free/")
os.system("conda config --add channels http://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/")
os.system("conda config --add channels http://mirrors.ustc.edu.cn/anaconda/cloud/msys2/")
os.system("conda config --add channels http://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/")
os.system("conda config --add channels http://mirrors.ustc.edu.cn/anaconda/cloud/menpo/")
os.system("conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/")
os.system("conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge")
os.system("conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/")
os.system("conda config --set show_channel_urls yes")
os.system("conda config --show-sources")
