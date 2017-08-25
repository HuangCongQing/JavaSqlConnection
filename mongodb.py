# -*- coding: utf-8 -*-
'''
Created on 2017年8月25日

@author: hasee
'''
# 使用MongoClient对象建立连接：
from pymongo import MongoClient
from itertools import product
client = MongoClient()
 
# 使用上面的代码片段，将建立连接到默认主机（localhost）和端口（27017）。您还可以指定主机和/或使用端口：
client = MongoClient('localhost', 27017)

# 或者使用MongoURl格式：
# client = MongoClient('mongodb://localhost:27017')

db = client.test  #连接mydb数据库，没有则自动创建
my_set = db.test_set #使用test_set集合，没有则自动创建

# my_set.insert({"name":"zhangsan","age":18})

#查询全部
# for i in my_set.find():
#     print(i)
db1 = client.taobao
product = db1.food


