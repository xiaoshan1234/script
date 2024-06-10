import sys,logging
import time
from pathlib import Path
import subprocess as sp
import re
from Tea.core import TeaCore
from typing import List
import configparser
from pathlib import Path

from alibabacloud_alidns20150109.client import Client as DnsClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_alidns20150109 import models as dns_models
from alibabacloud_tea_util.client import Client as UtilClient

dnsLogger = logging.getLogger("aliyun_dns_logger")
fileLogHandler = logging.FileHandler(filename=Path(__file__).parent / "ddns.log", mode="a+")
fileLogHandler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s'))
dnsLogger.addHandler(fileLogHandler)
dnsLogger.setLevel(logging.INFO)

class AliyunDnsService:
    def __init__(self):
        self.get_conf()
        return 

    # 读取配置
    def get_conf(self): 
        self.conf = configparser.ConfigParser()
        try:
            self.conf.read(Path(__file__).parent / "ddns.conf")
            self.target_host = self.conf["ddns"]["target_host"]
            self.target_domain = self.conf["ddns"]["target_domain"]
            self.aliyun_keyid = self.conf["ddns"]["aliyun_keyid"]
            self.aliyun_key_secret = self.conf["ddns"]["aliyun_key_secret"]
            self.record_type = "AAAA"
            dnsLogger.info("success")
        except KeyError as error:
            dnsLogger.error("error: connot find ",error)
        except configparser.NoSectionError as error:
            dnsLogger.error(error)
        except Exception as error:
            dnsLogger.error(error)  
        
        return   

    # 获取本地ip
    @staticmethod                
    def get_loacl_ipv6() -> str:
        if sys.platform.startswith('win'):
            cmdList = ["ipconfig"]
            ptnGlbIPv6 = re.compile(r"\n\s+IPv6 地址[\. \s]+:\s+(2[a-f0-9:]*)")
        elif sys.platform.startswith('lin'):
            cmdList = ["ip","a"]
            ptnGlbIPv6 = re.compile(r"inet6\s*(2[a-f0-9:]*)/")
        objCmpltProcess = sp.run(cmdList,capture_output=True,encoding="gb2312")
        rstSearch = ptnGlbIPv6.search(objCmpltProcess.stdout)
        if rstSearch:
            dnsLogger.info("success")
            return rstSearch.group(1)
        else:
            return None
        
    @staticmethod           
    def get_dns_client(aliyun_keyid:str, aliyun_key_secret:str)->DnsClient:
        config = open_api_models.Config()
        config.access_key_id = aliyun_keyid # 您的AccessKey ID
        config.access_key_secret = aliyun_key_secret # 您的AccessKey Secret
        return DnsClient(config)
    
    @staticmethod  
    def query_domain(dns_client : DnsClient,
                     target_domain:str, 
                     target_host:str, 
                     record_type:str):
        """
        获取主域名的所有解析记录列表
        """
        req = dns_models.DescribeDomainRecordsRequest()
        req.domain_name = target_domain # 主域名
        req.rrkey_word = target_host # 主机记录
        req.type = record_type # 解析记录类型
        
        try:
            resp = dns_client.describe_domain_records(req)
            dnsLogger.debug('-------------------获取主域名的所有解析记录列表--------------------')
            dnsLogger.debug(UtilClient.to_jsonstring(TeaCore.to_map(resp)))
            dnsLogger.info("success")
            dnsLogger.info(resp.body.domain_records.record[0].value)
            return resp
        except Exception as error:
            dnsLogger.error(error.message)
        return None
    
    @staticmethod 
    def update_domain_record(dns_client : DnsClient,
                        target_host:str,
                        record_type:str,
                        record_id:str,
                        target_ip:str ):
        """
        修改解析记录
        """
        try:
            req = dns_models.UpdateDomainRecordRequest()
            req.record_id = record_id
            req.rr = target_host
            req.value = target_ip
            req.type = record_type
            resp =dns_client.update_domain_record(req)
            dnsLogger.debug('-------------------修改解析记录--------------------')
            dnsLogger.debug(UtilClient.to_jsonstring(TeaCore.to_map(resp)))
            dnsLogger.info("success")
        except Exception as error:
            dnsLogger.error(error.message)  

    @staticmethod 
    def add_domain_record(dns_client : DnsClient,
                          target_domain:str, 
                          target_host:str, 
                          record_type:str, 
                          target_ip:str):
        """
        AddDomainRecord  添加域名解析记录
        @param client:            客户端
        @param domain_name:        域名名称
        @param rr:                主机记录
        @param record_type:              记录类型(A/NS/MX/TXT/CNAME/SRV/AAAA/CAA/REDIRECT_URL/FORWARD_URL)
        @param value:             记录值
        @throws Exception
        """
        req = dns_models.AddDomainRecordRequest()
        req.domain_name = target_domain
        req.rr = target_host
        req.type = record_type
        req.value = target_ip
        try:
            resp = dns_client.add_domain_record(req)
            dnsLogger.debug(f'添加域名解析记录的结果(json)↓')
            dnsLogger.debug(UtilClient.to_jsonstring(TeaCore.to_map(resp)))
            dnsLogger.info("success")
        except Exception as error:
            dnsLogger.error(error.message)

    def run(self):
        try:
            self.ipv6 = AliyunDnsService.get_loacl_ipv6()
            self.dns_client = AliyunDnsService.get_dns_client(self.aliyun_keyid,
                                                              self.aliyun_key_secret)
            resp = AliyunDnsService.query_domain(self.dns_client,
                                     self.target_domain,
                                     self.target_host,
                                     self.record_type)
            if resp is None:
                AliyunDnsService.add_domain_record(self.dns_client,
                                     self.target_domain,
                                     self.target_host,
                                     self.record_type,
                                     self.ipv6)  
            else:
                self.record_id = resp.body.domain_records.record[0].record_id
                self.remote_ipv6 = resp.body.domain_records.record[0].value                            
            while True:
                self.ipv6 = AliyunDnsService.get_loacl_ipv6()
                if self.ipv6 != self.remote_ipv6:
                    dnsLogger.info("local  ipv6: ",self.ipv6)
                    dnsLogger.info("remote ipv6: ",self.remote_ipv6)
                    AliyunDnsService.update_domain_record(self.dns_client,
                                     self.target_host,
                                     self.record_type,
                                     self.record_id,
                                     self.ipv6)
                    resp = AliyunDnsService.query_domain(self.dns_client,
                                     self.target_domain,
                                     self.target_host,
                                     self.record_type)
                    self.remote_ipv6 = resp.body.domain_records.record[0].value                       
                    
                time.sleep(60)      
        except Exception as e:
            dnsLogger.error(e)

if __name__ == "__main__":
    objAliyunDnsService = AliyunDnsService()
    objAliyunDnsService.run()
