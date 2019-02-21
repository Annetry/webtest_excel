#coding:utf-8
import os

import requests
# header={
#     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
#     "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
# }
# def post2(url,data):
#     r=requests.post(url=url,data=data,headers=header,timeout=10)
#     return r2

def dir_base(packagename):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),packagename)

