#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************************#
# Function:提示和传递 
#***************************************************************#

from sys import argv

script,user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a feww questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print """
Alright, so you said %s about liking me.
You live in %s.
""" % (likes,lives)



"""
#./lesson14.py wlt
Hi wlt, I'm the ./lesson14.py script.
I'd like to ask you a feww questions.
Do you like me wlt?
> yeah
Where do you live wlt?
> hangzhou

Alright, so you said yeah about liking me.
You live in hangzhou.

当你运行这个脚本时，记住你需要把你的名字赋给这个脚本，让 argv 参数接收到你的名称。
三个引号 """ 可以定义多行字符串，而 % 是字符串的格式化工具。
"""
