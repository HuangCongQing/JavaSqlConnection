# -*- coding: utf-8 -*-
'''
Created on 2017年8月18日

@author: 黄重庆
'''
import requests
from bs4 import BeautifulSoup
import re
import time
# 请在豆瓣任意找一本图书，抓取它某一页的短评并进行页面解析将短评文字抽取后输出，再对其中的评分进行抽取计算其总分。
# bookid换成自己选择的书名id
# sum = 0
# r = requests.get('https://book.douban.com/subject/6038371/comments/')
# # r = requests.get('https://book.douban.com/subject/bookid/comments/')
# soup = BeautifulSoup(r.text, 'lxml')
# pattern = soup.find_all('p', 'comment-content')
# for item in pattern:
#     print(item.string)
# pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
# p = re.findall(pattern_s, r.text)
# for star in p:
#     sum += int(star)
# print("----JavaScript DOM编程艺术 （第2版）-------")
# print(sum)

# 1.    “迷你爬虫编程小练习”进阶：抽取某本书的前50条短评内容并计算评分的平均值。


# count = 0
# i = 0
# sum, count_s = 0, 0
# while(count < 50):
#     try:
#         r = requests.get('https://book.douban.com/subject/6038371/comments/hot?p=' + str(i+1))
#     except Exception as err:
#         print(err)
#         break
#     soup = BeautifulSoup(r.text, 'lxml')
#     comments = soup.find_all('p', 'comment-content')
#     for item in comments:
#         count = count + 1
#         print(count, item.string)
#         if count == 50:
#             break  
#     pattern = re.compile('<span class="user-stars allstar(.*?) rating"')
#     p = re.findall(pattern, r.text)
#     for star in p:
#         count_s = count_s + 1
#         sum += int(star)
#     time.sleep(5)    # delay request from douban's robots.txt
#     i += 1
# if count == 50:
#     print(sum / count_s)



# 2.    在“http://money.cnn.com/data/dow30/”上抓取道指成分股数据并将30家公司的代码、公司名称和最近一次成交价放到一个列表中输出。



def retrieve_dji_list():
    r = requests.get('http://money.cnn.com/data/dow30/')
    search_pattern = re.compile('class="wsod_symbol">(.*)<\/a>.*<span.*">(.*?)<\/span>.*\n.*class="wsod_stream">(.*)<\/span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    return dji_list_in_text

dji_list = retrieve_dji_list()
print(dji_list)




