#NOTSET
#DEBUG
#INFO
#WARNING
#ERROR
#CRITICAL
import logging
from pathlib import Path
myLogger = logging.getLogger("MyLogger")
fileHandler = logging.FileHandler(filename=Path(__file__).parent / "ddns.log", mode="a+")
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileHandler.setFormatter(file_format)
myLogger.addHandler(fileHandler)
myLogger.setLevel(logging.INFO)


myLogger.info("hello")
myLogger.info("world") 
myLogger.error("error") 