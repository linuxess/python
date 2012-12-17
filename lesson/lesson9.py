#!/usr/bin/python
#-*- coding:utf-8 -*-

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There,s something going one here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""







"""
#./lesson9.py 
Here are the days:  Mon Tue Wed Thu Fri Sat Sun
Here are the months:  Jan
Feb
Mar
Apr
May
Jun
Jul
Aug

There,s something going one here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.


为什么使用 %r 时 \n 新行就不灵了？
%r 就是这个样子，它打印出的是你写出来的方式（或者近似方式）。它是用来 debug 的原始格式。
为什么你打印时用了 + 而不是逗号？
因为我的目的是将两个字符串连接起来，组建成一个新的字符串。后面你会学到，print 里的逗号其实是分隔参数的一种方式。
"""
