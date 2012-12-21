#!/usr/bin/python
#-*- coding:utf-8 -*-
# ScriptName: less28_boolean.py


"""
example:
3 != 4 and not ("testing" != "test" or "Python" == "Python")
Here's me going through each of the steps and showing you the translation until I've boiled it down to a single result:

    Solve each equality test:
    3 != 4 is True: True and not ("testing" != "test" or "Python" == "Python")
    "testing" != "test" is True: True and not (True or "Python" == "Python")
    "Python" == "Python": True and not (True or True)
    Find each and/or in parenthesis ():
    (True or True) is True: True and not (True)
    Find each not and invert it:
    not (True) is False: True and False
    Find any remaining and/or and solve them:
    True and False is False
    With that we're done and know the result is False.
"""


"""
Is there any difference between != and <>?
Python has deprecated <> in favor of !=, so use !=. Other than that there should be no difference.

