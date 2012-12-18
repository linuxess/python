#!/usr/bin/python
#-*- coding:utf-8 -*-

print "How old are you?", 
age = raw_input()
print "How tall are you?"
height = raw_input()

print "so, you'er %s old, %s tall." % (age,height)



"""
#./lesson11.py 
How old are you? 23
How tall are you?
158
so, you'er 23 old, 158 tall.
print 后面加了个逗号(comma) print 就不会输出新行符而结束这一行跑到下一行去了。
"""

"""
改进版：
age = raw_input("How old are you?")
height = raw_input("How tall are you?")

print "so, you'er %s old, %s tall." % (age,height)
"""


