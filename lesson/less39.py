#!/usr/bin/python
#-*- coding:utf-8 -*-
# Function:Dictionaries, Oh Lovely Dictionaries 
# ScriptName: less39.py
#***************************************************************#
#如果说类和迷你模块差不多，那么对于类来说，也必然有一个类似 import 的概念。这个概念名称就是“实例(instance)”。
#这只是一种故作高深的叫法而已，它的意思其实是“创建”。当你将一个类“实例化”以后，你就得到了一个 对象(object) 。

class song(object):
    
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

#song的参数传进来，调用sone里面定义的函数时就可以用这些参数
happy_bday = song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()


"""
#./less39.py 
Happy birthday to you
I don't want to get sued
So I'll stop right there
They rally around the family
With pockets full of shells
"""

"""
为什么创建 __init__ 或者别的类函数时需要多加一个 self 变量？

如果你不加 self ， cheese = 'Frank' 这样的代码意义就不明确了，它指的既可能是实例的 cheese 属性，或者一个叫做 cheese 的局部变量。
有了 self.cheese = 'Frank' 你就清楚地知道了这指的是实例的属性 self.cheese 。
"""
