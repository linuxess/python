#!/usr/bin/python
#-*- coding:utf-8 -*-
# Function: Loops And Lists 
# ScriptName: less32.py

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pannies',2,'dimes',3,'quarters']

for number in the_count:
    print "this is count %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit

for i in change:
    print "i got %s" % i

#build lists, first start with an empty one
elements = []

#use the range function to do 0 to 5 counts
for i in range(0,6):
    print "adding %d to the list." % i
    elements.append(i)

#print them out too
for i in elements:
    print "Elements was: %d" % i


"""
#./less32.py 
this is count 1
this is count 2
this is count 3
this is count 4
this is count 5
A fruit of type: apples
A fruit of type: oranges
A fruit of type: pears
A fruit of type: apricots
i got 1
i got pannies
i got 2
i got dimes
i got 3
i got quarters
adding 0 to the list.
adding 1 to the list.
adding 2 to the list.
adding 3 to the list.
adding 4 to the list.
adding 5 to the list.
Elements was: 0
Elements was: 1
Elements was: 2
Elements was: 3
Elements was: 4
Elements was: 5
"""

"""
Why does for i in range(1, 3): only loop 2 times instead of 3 times?
The range() function only does numbers from the first to the last, not including the last. So it stops at 2, not 3 in the above. This turns out to be the most common way to do this kind of loop.
"""
