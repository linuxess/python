#!/usr/bin/python
#-*- coding:utf-8 -*-
# Function:命名、变量、代码、函数 
# ScriptName: lesson19_fun_var.py

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %s, arg2: %s" % (arg1, arg2)

def print_two_again(arg1,arg2):
    print "arg1: %s, arg2: %s" % (arg1,arg2)

def print_one(arg1):
    print "arg1: %s" % arg1

def print_none():
    print "I got nothing."

print_two("Zed", "Show")
print_two_again("zed", "show")
print_one("first")
print_none()



"""
#./lesson19_fun_var.py 
arg1: Zed, arg2: Show
arg1: zed, arg2: show
arg1: first
I got nothing.

*args 的 * 是什么意思？
它的功能是告诉 python 让它把函数的所有参数都接受进来，然后放到名字叫 args 的列表中去。和你一直在用的 argv 差不多，只不过前者是用在函数上面。没什么特殊情况，我们一般不会经常用到这个东西。
函数名称有什么规则？
和变量名一样，只要以字母数字以及下划线组成，而且不是数字开始，就可以了。
"""
