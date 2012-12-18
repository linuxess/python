#!/usr/bin/python
#-*- coding:utf-8 -*-

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first varibale is:", first
print "Your scond varible is:", second
print "Your third varible is:", third


"""
#./lesson13.py one two three
The script is called: ./lesson13.py
Your first varibale is: one
Your scond varible is: two
Your third varible is: three

script, first, second, third = argv ：把 argv 中的东
西解包，将所有的参数依次赋予左边的变量名

argv 和 raw_input() 有什么不同？
不同点在于用户输入的时机。如果参数是在用户执行命令时就要输入，那就是 argv， 如果是在脚本运行过程中需要用户输入，那就使用 raw_input()。

命令行参数是字符串吗？
是的，就算你在命令行输入数字，你也需要用 int() 把它先转成数字，和在 raw_input() 里一样。

"""
