#!/usr/bin/python
#-*- coding:utf-8 -*-
# Function:Doing Things To Lists 
# ScriptName: less38.py
#***************************************************************#

"""
字典中包含字典
"""

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 20
print "NY state has:", cities['NY']

print '-' * 20
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

print '-' * 20
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

print '-' * 20
for state, abbrev in states.items():
    print "%s is abbreviate %s" % (state, abbrev)

print '-' * 20
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

print '-' * 20
state = states.get('Texas', None)

if not state:
    print "Sorrry, no Texas"

city = cities.get('TX', 'Does Not Exist')
print "The city for the state TX is: %s" % city


"""
#./less38.py 
--------------------
NY state has: New York
--------------------
Michigan's abbreviation is:  MI
Florida's abbreviation is:  FL
--------------------
Michigan has:  Detroit
Florida has:  Jacksonville
--------------------
California is abbreviate CA
Michigan is abbreviate MI
New York is abbreviate NY
Florida is abbreviate FL
Oregon is abbreviate OR
--------------------
FL has the city Jacksonville
CA has the city San Francisco
MI has the city Detroit
OR has the city Portland
NY has the city New York
--------------------
Sorrry, no Texas
The city for the state TX is: Does Not Exist
"""


"""
$ python
Python 2.6.5 (r265:79063, Apr 16 2010, 13:57:41)
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> class Thing(object):
...     def test(hi):
...             print "hi"
...
>>> a = Thing()
>>> a.test("hello")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: test() takes exactly 1 argument (2 given)
>>>
