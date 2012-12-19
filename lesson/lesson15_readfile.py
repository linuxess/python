#!/usr/bin/python
#-*- coding:utf-8 -*-
# Function:读取文件

filename = 'ex15_example.txt'
f = open(filename)
print f.read()
f.close()



"""
#./lesson15.py 
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

open(filename) 返回的是文件的内容吗？
不是，它返回的是一个叫做“file object”的东西，你可以把它想象成一个磁带机或者DVD机。你 可以随意访问内容的任意位置，并且去读取这些内容，不过这个 object 本身并不是它的内容。

read() readline() readlines()的区别
.read() 每次读取整个文件，它通常将读取到底文件内容放到一个字符串变量中，也就是说 .read() 生成文件内容是一个字符串类型
.readline()每只读取文件的一行，通常也是读取到的一行内容放到一个字符串变量中，返回str类型
.readlines()每次按行读取整个文件内容，将读取到的内容放到一个列表中，返回list类型
另一方面，.readline() 每次只读取一行，通常比 .readlines() 慢得多。仅当没有足够内存可以一次读取整个文件时，才应该使用 .readline()
"""

