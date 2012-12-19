#!/usr/bin/python
#-*- coding:utf-8 -*-
# Function:函数和文件
# ScriptName: lesson19_fun_var.py

from sys import argv

script, input_file = argv

#fun print all
def print_all(f):
    print f.read()

#fun seek
def rewind(f):
    f.seek(0)

#fun print a line
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)     #go to the first line
print "Let's print three lines:"        #read line one by one
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)



"""
#./lesson19_fun_var.py example.txt 
aaaaaaaaa
bbbbbbbb
cccccccccc

Now let's rewind, kind of like a tape.
Let's print three lines:
1 aaaaaaaaa

2 bbbbbbbb

3 cccccccccc

seek(offset[, whence]) -> None.  Move to new file position.
seek 返回none，offset >=0 以字节为单位移动到新的位置。whence:0从起始位置移动，1从当前位置移动，2从结束位置移动.
     seek() 函数的处理对象是 字节 而非行，所以 seek(0) 只是转到文件的 0 byte，也就是第一个 byte 的位置。
+= 是什么？
英语里边 “it is” 可以写成 “it’s”，”you are” 可以写成 “you’re”，这叫做简写。而这个操作符是吧 = 和 + 简写到一起了。 x += y 的意思和 x = x + y 是一样的。
"""
