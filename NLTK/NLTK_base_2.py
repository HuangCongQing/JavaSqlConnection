# -*- coding: utf-8 -*-
'''
Created on 2017年8月21日

@author: hasee
'''
#古腾堡语料库
import nltk
nltk.corpus.gutenberg.fileids()

emma = nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma)


