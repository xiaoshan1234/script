from pathlib import Path
import  sys
import argparse
import subprocess

dcPipSrcHost = {
    'qs': 'pypi.tuna.tsinghua.edu.cn',
    'utsc': 'pypi.mirrors.ustc.edu.cn',
    'aliy': 'mirrors.aliyun.com'
}

dcPipSrcUrl = {
    'qs': 'https://pypi.tuna.tsinghua.edu.cn/simple',
    'ustc': 'https://pypi.mirrors.ustc.edu.cn/simple',
    'aliy': 'http://mirrors.aliyun.com/pypi/simple/'
}

if "__main__" == __name__:
    parser = argparse.ArgumentParser(description='change pip source.')
    parser.add_argument('-s', '--source', type=str, choices=["qs","utsc","aliy"], default='qs', help='qs  or utsc')
    args = parser.parse_args()

    if sys.platform.startswith('win'):
        fpPipConf = Path("~/pip/pip.ini").expanduser()
    elif sys.platform.startswith('lin'):
        fpPipConf = Path("~/.pip/pip.conf").expanduser()

    if not fpPipConf.parent.exists():
        fpPipConf.parent.mkdir(parents=True)

    with fpPipConf.open('w') as fdPipConf:
        fdPipConf.write('[global]\n')
        fdPipConf.write(f'trusted-host = {dcPipSrcHost[args.source]}\n')
        fdPipConf.write(f'index-url = {dcPipSrcUrl[args.source]}')

    subprocess.run(["pip","config","set","global.index-url",dcPipSrcUrl[args.source]])             
    subprocess.run(["pip","config","set","global.trusted-host",dcPipSrcHost[args.source]])     
    subprocess.run(["pip","config","list"])        
                                
                        









