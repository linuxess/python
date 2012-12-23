#!/usr/bin/python
#-*- coding:utf-8 -*-
# Function:Dictionaries, Oh Lovely Dictionaries 
# ScriptName: less39.py
#***************************************************************#

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

