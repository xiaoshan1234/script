#! 
from pathlib import Path
import logging,sys

# log
mainlog = logging.getLogger("Mainlog")
logHandler = logging.StreamHandler(sys.stdout)
logFormat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logHandler.setFormatter(logFormat)
mainlog.addHandler(logHandler)
mainlog.setLevel(logging.INFO)

# 文件的操作


# 遍历
targetDirs = [Path("./"),]

supportQueue = []
supportStack = []
blackTable = [".git"]
whiteTable = []


# 广度遍历
def do_node(curNode:Path)->None:
    if curNode.is_dir():
        print("dir ", curNode)
    else:
        print("file ", curNode)
    return 

    
def push_children_to_queue(curNode:Path, supportQueue:list)->None:
    if curNode.is_dir():
        for child in curNode.iterdir():
            if child.name in blackTable:
                pass
            else:
                supportQueue.append(child)
    return 


def traverse_width(curNode:Path, supportQueue:list)->None:
    do_node(curNode)
    push_children_to_queue(curNode,supportQueue)
    if 0 != len(supportQueue):
        nextNode = supportQueue.pop(0)
        traverse_width(nextNode,supportQueue)
    return 


for rootPath in targetDirs:
    supportQueue = []
    if rootPath.exists():
        traverse_width(rootPath,supportQueue)
    else:
        mainlog.info("this path do not exsit!",rootPath)
        break
    


# 深度遍历
