# -*-coding:utf-8-*-
__author__ = 'ccz'

import web
import conmongo
import sys
import json
import re
from json import *
import urllib
reload(sys)
sys.setdefaultencoding('utf-8')

##urls (argument) - class - page
urls = (
    '/(\index)', 'index',
    '/graph','graph'

)
render = web.template.render("templates")


class index:
    def GET(self, name):
        return render.index(name)

    def POST(self, name):
        i = web.data()
        topic = i.split('=')[1]
        topic = urllib.unquote(topic)
        # 获取公司数据
        info = getBaseInfo(topic)
        return render.graph(name, topic,info)
        # return render.graph(name, topic,  'info')

class graph:
    def GET(self, name):
        return render.graph(name)

    def POST(self):
        i = web.data()
        i =urllib.unquote(i)
        print i
        topic = i.split('=')[1]
        type =i.split('=')[2]
        file_object = open('1.json')
        strdata1 = eval(file_object.read())
        try:
            data1 = json.dumps(strdata1)
        finally:
            file_object.close()
        # 获取数据

        return data1

def getBaseInfo(name):
        data = {"$or":[{"公司名称": {'$regex': name}},{"A股代码":name}]}
        processor = conmongo.process()
        rows = processor.queryData(data)
        res =''
        for row in rows:
            for key in row.keys():  # 遍历字典
                res += str(key) + ":" + str(row[key]) + "\n"

        return res

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
