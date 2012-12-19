#!/usr/bin/python
#-*- coding:utf-8 -*-
# ScriptName: lessone24.py

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print "-" * 40
print poem
print "-" * 40

def secret(started):
    jelly = started * 500
    jars = jelly / 100
    return jelly, jars

start_point = 10000
je, ja = secret(start_point)

print "With a starting point of: %d" %start_point
print "We'd have %s jelly, %d jars" %(je, ja)

start_point = start_point / 10
print "We'd have %s jelly, %d jars" % secret(start_point)



"""
#./lesson24.py 
----------------------------------------

    The lovely world
    with logic so firmly planted
    cannot discern 
     the needs of love
     nor comprehend passion from intuition
     and requires an explanation

            where there is none.

----------------------------------------
With a starting point of: 10000
We'd have 5000000 jelly, 50000 jars
We'd have 500000 jelly, 5000 jars

A&&Q
How come you call the variable jelly/jars the name je/ja later?
That's part of how a function works. Rememer that inside the function the variable is temporary, and when you return it then it can be assigned to a variable for later. I'm just making a new variable named beans to hold the return value.
"""
