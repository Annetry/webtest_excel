#coding:utf-8
import json
import os
import xlrd
class GetUrlData(object):
    def getdir(self,filename):
        path=os.path.join(os.path.dirname(__file__),filename)
        return path
    def getsheet(self,rowx,sheet='0'):
        '''读取excel数据
        ；paramet：index 读取sheet的索引；rowx 输入读取的行号'''
        sht=xlrd.open_workbook(self.getdir('urldata.xlsx'))
        table=sht.sheet_by_index(int(sheet))
        return table.row_values(rowx)
    def getUrl(self,rowx):
        '''获取excel的第2列索引为1的URL数据，类型为str'''
        return self.getsheet(rowx,0)[1]
    def getData(self,rowx):
        '''获取excel的第3列索引为2的Data数据，转行为dict类型'''
        return json.loads(self.getsheet(rowx)[2])

# y=GetUrlData()
# print(y.getUrl(1))
# print(type(y.getData(1)))