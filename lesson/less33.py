#!/usr/bin/python
#-*- coding:utf-8 -*-
# Function:While Loops 
# ScriptName: less33.py
#***************************************************************#

i = 0
numbers = []

while i < 6:
    print "at the top i is %d" % i
    numbers.append(i)
    i += 1
    print "numbers now:", numbers
    print "at the bottom i is %d" % i

print "the numbers:"
for num in numbers:
    print num


"""
#./less33.py 
at the top i is 0
numbers now: [0]
at the bottom i is 1
at the top i is 1
numbers now: [0, 1]
at the bottom i is 2
at the top i is 2
numbers now: [0, 1, 2]
at the bottom i is 3
at the top i is 3
numbers now: [0, 1, 2, 3]
at the bottom i is 4
at the top i is 4
numbers now: [0, 1, 2, 3, 4]
at the bottom i is 5
at the top i is 5
numbers now: [0, 1, 2, 3, 4, 5]
at the bottom i is 6
the numbers:
    0
    1
    2
    3
    4
    5
"""


"""
What's the difference between a for-loop and a while-loop?
A for-loop can only iterate (loop) "over" collections of things. A while-loop can do any kind of iteration (looping) you want. However, while-loops are harder to get right and you normally can get many things done with for-loops.
"""
