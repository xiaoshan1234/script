import os

ai_lib = "tensorflow-gpu=2.6.0 opencv matplotlib numpy "
os.system("conda create -n AI python==3.8 -y")
os.system("conda activate AI")
os.system("conda install " + ai_lib + " -y")
