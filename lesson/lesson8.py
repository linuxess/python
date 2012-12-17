#!/usr/bin/python
#-*- coding: utf-8 -*-

formatter = "%r %r %r"

print formatter % (1,2,3)
print formatter % ("one","two","three")
print formatter % (True,False,True)
print formatter % (formatter,formatter,formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing."
)





"""
#./lesson8.py 
1 2 3
'one' 'two' 'three'
True False True
'%r %r %r' '%r %r %r' '%r %r %r'
'I had this thing.' 'That you could type up right.' "But it didn't sing."
我应该使用 %s 还是 %r？
你应该使用 %s，只有在想要获取某些东西的 debug 信息时才能用到 %r。 %r 给你的是变量的“程序员原始版本”，又被称作“representation”。
为什么 %r 有时打印出来的是单引号，而我实际用的是双引号？
Python 会用最有效的方式打印出字符串，而不是完全按照你写的方式来打印。这样做对于 %r 来说是可以接受的，因为它是用作 debug 和排错，没必要非打印出多好看的格式。
"""
