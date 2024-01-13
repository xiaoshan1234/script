from pathlib import *
import img2pdf
import argparse
from PIL import Image
import numpy as np

if "__main__" == __name__ :
    myArgParser = argparse.ArgumentParser(description = """a transformer bettween base64 and hex""")
    myArgParser.add_argument("fp", 
                            type = str, 
                            help = "file path")
    myArgParser.add_argument("--pg", 
                            type = int, 
                            help = "page num")
    myArgs = myArgParser.parse_args()

    srcFp = Path(myArgs.fp)
    pgNum = myArgs.pg if myArgs.pg else 1

    if not srcFp.exists():
        print(f"{srcFp} File not found!")
        exit()

    srcFp = srcFp.absolute()
    tgtFp = Path(__file__).absolute().with_name(srcFp.stem + ".pdf")

    if pgNum == 1:
        with open(tgtFp,mode="wb") as tgtFd:
            tgtFd.write(img2pdf.convert(str(srcFp)))
    else:
        npSrcImage = np.array(Image.open(str(srcFp)))

        lenPerImg = npSrcImage.shape[0] // pgNum
        for i in range(pgNum - 1):
            Image.fromarray(npSrcImage[i*lenPerImg:(i+1)*lenPerImg,:,:]).save("./temp_{num}.png".format(num=i+1))
        
        Image.fromarray(npSrcImage[(pgNum - 1)*lenPerImg:,:,:]).save("./temp_{num}.png".format(num=pgNum))

        fplistTmpImg = Path(__file__).parent.glob("./temp_*.png")

        with open(tgtFp,mode="wb") as tgtFd:
            tgtFd.write(img2pdf.convert(list(fplistTmpImg)))
        
    print(f"Converted {srcFp} to {tgtFp}")