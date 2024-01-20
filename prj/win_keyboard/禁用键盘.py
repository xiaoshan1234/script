import os 

with os.popen(" sc config i8042prt start= disabled") as op_file:
    rst = op_file.read()

print(rst)