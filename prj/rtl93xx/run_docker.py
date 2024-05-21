import re
import argparse
import subprocess as sp
import pathlib
# myArgParser = argparse.ArgumentParser(description = "")

# myArgParser.add_argument("type", 
#                          type = str, 
#                          choices = ["hex",],
#                          help = "Data Format")

# myArgs = myArgParser.parse_args()

ptnDocker = re.compile(r"groups=.*(docker)")


if "__main__" == __name__ :
    try:
        print("id")
        p1 = sp.Popen(args=['id'], stdout=sp.PIPE, shell=False)
    except Exception as e:
        print("Error:", str(e))

    strRet = p1.stdout.read()
    if ptnDocker.search(strRet):
        try:
            p2 = sp.run(args=strRunDocker.split(sep=" "), stdout=sp.PIPE, shell=True)
        except Exception as e:
            print("Error:", str(e))
    else:
        print("you are not in docker group")
        print("you can run 'usermod -aG docker [your username]' to add yourself to the docker group")

