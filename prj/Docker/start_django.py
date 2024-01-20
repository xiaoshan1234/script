import os
import time
#执行你的脚本
os.system("nginx -c /etc/nginx/nginx.conf")
os.system("/usr/local/bin/uwsgi --ini /var/www/MainWebsite/uwsgi/uwsgi.ini")

#无线循环
while True:
    print("Now Time",time.ctime())
    time.sleep(12*60*60)

