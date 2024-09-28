#NOTSET
#DEBUG
#INFO
#WARNING
#ERROR
#CRITICAL
import logging
from pathlib import Path
myLogger = logging.getLogger("MyLogger")

logHandler = logging.FileHandler(filename=Path(__file__).parent / "ddns.log", mode="a+")
logFormat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logHandler.setFormatter(logFormat)

myLogger.addHandler(logHandler)
myLogger.setLevel(logging.INFO)


myLogger.info("hello")
myLogger.info("world") 
myLogger.error("error") 