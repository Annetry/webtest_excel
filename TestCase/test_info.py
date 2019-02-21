#coding:utf-8
import requests
import unittest
from WEB_exceldata.Packaging import *
from WEB_exceldata.Data.getExcel import *
import re

class TestUser(unittest.TestCase,GetUrlData):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_login(self):
        s=requests.Session()
        mm=s.post(self.getUrl(1),self.getData(1),verify=False)
        return s
    def statuscode(self,r):
        self.assertEqual(r.status_code,200)
    def set_token(self):
        r=self.test_login().get(self.getUrl(2))
        #<a href="http://www.renren.com/Logout.do?requesttoken=-247078222"><span class="ui-icon,正则后:['-247078222']
        pattern=re.compile(r'token=(.*)\"><span')
        mm=pattern.findall(r.text)
        token=''.join(mm)
        self.statuscode(r)
        #必须赋予中间值，将返回的token赋予表格中
        dict2=self.getData(2)
        dict2['token']=token
        return dict2

if __name__=="__main__":
    unittest.main(verbosity=2)

