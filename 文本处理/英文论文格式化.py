import re

source_path = "text.txt"
new_path = "new." + source_path

with open(source_path,"r",encoding='utf-8') as source_file:
    with open(new_path,mode='w',encoding='utf-8')  as new_file:
        
        s_text = source_file.read()
        s_text = re.sub(pattern = r"\[.*?\]",repl="",string=s_text,count=0)
        for c in s_text:
            if c == '\n': # 换行转空格
                new_file.write(' ')
            elif ord(c) in range(0x00,0x20):#控制字符去掉
                pass
            else:
                new_file.write(c)
            

    
    



    

