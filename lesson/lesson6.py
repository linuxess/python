#!/usr/bin/python
#-*- coding:utf-8 -*-

x = "There are %d types of pepple" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." %x
print "I also said: '%s'" % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e


'''
#./lesson6
There are 10 types of pepple
Those who know binary and those who don't.
I said: 'There are 10 types of pepple'.
I also said: 'Those who know binary and those who don't.'
Isn't that joke so funny?! False
This is the left side of ...a string with a right side.
%r 和 %s 有什么不同？
%r 用来做 debug 比较好，因为它会显示变量的原始数据（raw data），而其它的符号则是用来向用户显示输出的。
'''
