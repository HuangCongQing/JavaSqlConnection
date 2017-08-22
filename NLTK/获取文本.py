# -*- coding: utf-8 -*-
'''
Created on 2017年8月21日

@author: hasee
'''

#txt在线文档下载
from urllib import urlopen
url = "http://www.gutenberg.org/files/2554/2554.txt"
response = urlopen(url)
raw = response.read().decode('utf8')
print( type(raw))

