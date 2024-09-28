from pathlib import Path
import subprocess as sp

print(__file__)
scriptPath = Path(__file__)
print("scriptPath: ",scriptPath)
prjRootPath = Path(scriptPath.parents[2])
print(prjRootPath)
prjDrvPath = Path(scriptPath.parents[1])
print(prjDrvPath)

# 8382l 
buildToolPath = Path(scriptPath.parents[0].joinpath("tool"))
print(buildToolPath,buildToolPath.exists())
if (False == buildToolPath.exists()):
    buildToolPath.symlink_to(target=r"C:\Users\l30997\Desktop\script\test", target_is_directory=True)
    
