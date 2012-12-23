#!/usr/bin/python
#-*- coding:utf-8 -*-
# Function:Learning To Speak Object Oriented
# ScriptName: less40.py
#***************************************************************#
#必操心为什么你的 class 要在后面添一个(object) ，只要跟着这样做就可以了

class TheThing(object):

    def __init__(self):
        self.number = 0

    def some_function(self):
        print "i got called"

    def add_me_up(self, more):
        self.number += more
        return self.number

a = TheThing()
b = TheThing()

print a.add_me_up(20)
print b.add_me_up(30)

print a.number
print b.number

class TheMultiplier(object):

    def __init__(self, base):
        self.base = base

    def do_it(self, m):
        return m * self.base

x = TheMultiplier(a.number)
print x.do_it(b.number)

"""
#./less41.py 
20
30
20
30
600
"""

"""
，它就是 Python 创建的额外的一个参数，有了它你才能实现 a.some_function()` 这种用法，这时它就会把\ 前者翻译成 ``some_function(a) 执行下去。为什么用 self 呢？因为你的函数并不知道你的这个“实例”是来自叫 TheThing 或者别的名字的 class。所以你只要使用一个通用的名字 self 。这样你写出来的函数就会在任何情况下都能正常工作。

其实你可以使用 self 以外的别的字眼，不过如果你这样做的话，你就会成为所有Python 程序员的众之矢的，所以还是随大流的好。只有变态才会在这里乱改，我教你的没错。对以后会读到你的代码的人好点儿，因为你现在的代码10年以后所有的代码都会是一团糟。
"""
