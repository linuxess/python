#!/usr/bin/python
#-*- coding:utf-8 -*-
# Function:write file 
# ScriptName: lesson16_writefile.py
#***************************************************************#

from sys import argv

script,filename = argv

print "erase %s" % filename
print "Opening the file..."
target = open(filename,'w')

print "Truncating the file..."
target.truncate()                  

print "Now I'm going to ask you for three lines."
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file"
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "Finally,we close it."
target.close()



"""
#./lesson16_writefile.py example.txt 
erase example.txt
Opening the file...
Truncating the file...
Now I'm going to ask you for three lines.
line1: aaaaaaaaa
line2: bbbbbbbb
line3: cccccccccc
I'm going to write these to the file
Finally,we close it.

close – 关闭文件。跟你编辑器的 文件->保存.. 一个意思。
read – 读取文件内容。你可以把结果赋给一个变量。
readline – 读取文本文件中的一行。
truncate – 清空文件，请小心使用该命令。
write(stuff) – 将stuff写入文件。
"""



