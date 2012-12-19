#!/usr/bin/python
#-*- coding:utf-8 -*-
# Function:函数返回值 
# ScriptName: lesson20.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

ad = add(20, 5)
su = subtract(20, 4)

print "%s, %s" % (ad, su)
print add(20, subtract(10, 5))


"""
#./lesson20.py 
25, 16
25
"""
