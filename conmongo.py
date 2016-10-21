# -*-coding:utf-8-*-
import pymongo
from pymongo import MongoClient
class DBConn:
    conn = None
    db = None
    # servers = "mongodb://localhost:27017/"

    def connect(self):
        self.conn = MongoClient('192.168.1.113',27017)
        # self.conn = MongoClient('192.168.1.133',27017)
        # self.conn=MongoClient()
        # self.conn.test.authenticate("dba", "dba")
        self.db=self.conn['data_105']
        # self.db=self.conn['test']

    def close(self):
        return self.conn.close()

    def getDb(self):
        return self.db

    def getConn(self):
        return self.conn

class process:
    db =None
    def __init__(self):
        # 建立连接
        dbconn = DBConn()
        dbconn.connect()
        conn = dbconn.getConn()
        self.db = dbconn.getDb()
        print conn.server_info()

    def insertDatas(self,name,data):
        self.name.table.insert(data)

    def updateData(self,name,data):
        # 只修改最后一条匹配到的数据
        #        第3个参数设置为True,没找到该数据就添加一条
        #        第4个参数设置为True,有多条记录就不更新
        # self.db.name.update({'name': 'steven1'}, {'$set': {'realname': '测试1修改'}}, False, False)
        self.db.name.update(data[0],data[1], False, False)

    def deleteData(self,name,data):
        # self.db.name.remove({'name': 'steven1'})
        self.db.name.remove(data)

    def queryData(self,name,data):
        # 查询全部数据
        rows = self.db.company.find(data)
        # self.printResult(rows)
        return rows
        # 查询一个数据
        # print db.lifeba.find_one()
        # 带条件查询
        # printResult(db.lifeba.find({'name': 'steven2'}))
        # printResult(db.lifeba.find({'name': {'$gt': 25}}))

    def printResult(self,rows):
        for row in rows:
            for key in row.keys():  # 遍历字典
                print str(key)+":"+str(row[key])
                print ''

