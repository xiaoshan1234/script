from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.DescribeSubDomainRecordsRequest import DescribeSubDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
import requests
from urllib.request import urlopen
import json
# IPv6 地址[\.\s]+:(240[a-f0-9:]*)
import os,re
def get_my_ipv6():
    try:
        with os.popen("ipconfig","r") as cmd_stream:
            cmd_reply = cmd_stream.read()
        sc_result = re.search(r"\n\s+IPv6 地址[\.\s]+:\s+(240[a-f0-9:]*)",cmd_reply)
        ipv6 = sc_result.group(1)
    except Exception:
        ipv6 = None
        print("ipv6 get fail")
    return ipv6

accessKeyId = ""  # 将accessKeyId改成自己的accessKeyId
accessSecret = ""  # 将accessSecret改成自己的accessSecret
domain = "xiaoshan12138.top"  # 你的主域名
sub_domain = "xbw"  # 要进行ipv6 ddns解析的子域名
log_file = "./aliddns.log"

client = AcsClient(accessKeyId, accessSecret, 'cn-hangzhou')

def update(RecordId, RR, Type, Value):  # 修改域名解析记录
    from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
    request = UpdateDomainRecordRequest()
    request.set_accept_format('json')
    request.set_RecordId(RecordId)
    request.set_RR(RR)
    request.set_Type(Type)
    request.set_Value(Value)
    response = client.do_action_with_exception(request)

def add(DomainName, RR, Type, Value):  # 添加新的域名解析记录
    from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest import AddDomainRecordRequest
    request = AddDomainRecordRequest()
    request.set_accept_format('json')
    request.set_DomainName(DomainName)
    request.set_RR(RR)  # https://blog.zeruns.tech
    request.set_Type(Type)
    request.set_Value(Value)    
    response = client.do_action_with_exception(request)

def add_or_update(ipv6,log_file):
    with open(log_file,"a+",encoding="utf-8") as op_file:
        op_file.write("time:{}, local_ipv6:{}\n".format(time.ctime(),ipv6))
        request = DescribeSubDomainRecordsRequest()
        request.set_accept_format('json')
        request.set_DomainName(domain)
        request.set_SubDomain(sub_domain + '.' + domain)
        request.set_Type("AAAA")
        response = client.do_action_with_exception(request)  # 获取域名解析记录列表
        domain_list = json.loads(response)  # 将返回的JSON数据转化为Python能识别的

        if domain_list['TotalCount'] == 0: # 没有此域名时添加此域名
            add(domain, sub_domain, "AAAA", ipv6)
            op_file.write("time:{}, 新建域名解析成功\n".format(time.ctime()))
        elif domain_list['TotalCount'] == 1: # 有此域名时更新此域名
            if domain_list['DomainRecords']['Record'][0]['Value'].strip() != ipv6.strip():
                update(domain_list['DomainRecords']['Record'][0]['RecordId'], sub_domain, "AAAA", ipv6)
                op_file.write("time:{}, 修改域名解析成功\n".format(time.ctime()))
            else:  # https://blog.zeruns.tech
                op_file.write("time:{}, IPv6地址没变\n".format(time.ctime()))
        elif domain_list['TotalCount'] > 1: # 有多个此域名时，删除后重新添加
            from aliyunsdkalidns.request.v20150109.DeleteSubDomainRecordsRequest import DeleteSubDomainRecordsRequest
            request = DeleteSubDomainRecordsRequest()
            request.set_accept_format('json')
            request.set_DomainName(domain)
            request.set_RR(sub_domain)  # https://blog.zeruns.tech
            request.set_Type("AAAA") 
            response = client.do_action_with_exception(request)
            add(domain, sub_domain, "AAAA", ipv6)
            op_file.write("time:{}, 修改域名解析成功\n".format(time.ctime()))

# 开始循环
ipv6 = get_my_ipv6()
ipv6_in_remote = "" #假设这就是远端的ipv6
import time
while True:
    if ipv6 and (ipv6 != ipv6_in_remote): #有ipv6且ipv6有更新时再向云端提交更新
        add_or_update(ipv6,log_file=log_file)
        ipv6_in_remote = ipv6
    
    ipv6 = get_my_ipv6()

    time.sleep(60)

    
    

