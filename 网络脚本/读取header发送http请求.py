import chardet
import time
import requests
import fake_useragent
def read_header_from_file(filename:str):
    with open(filename,"r") as myfile:
        txt = myfile.read()
        txt = txt.replace(" ","")
    items = txt.split('\n')
    header = {}
    for one in items:
        key,value = one.split(':',maxsplit=1)
        header[key] = value

    return header
if __name__ == '__main__':
    myheader = read_header_from_file("./web_manage/header.txt")
    myheader['user-agent'] = fake_useragent.UserAgent().random
    print(myheader)
    while True:
        try:
            result = requests.get(headers=myheader,url="https://www.nwxs8.com/news/page_4.html")
            time.sleep(1)
            break
        except OSError as e:
            print(e)
        continue

    charset = chardet.detect(result.content)
    result.encoding = charset['encoding']

    print(result.text)



    