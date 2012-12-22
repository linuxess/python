#!/usr/bin/python
#-*- coding:utf-8 -*-
# ScriptName: less25_module.py

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split()
    return words

def sort_words(words):
    """sorts the words"""
    return sorted(words)

def print_first_word(words):
    """print the first word after popping it off"""
    word = words.pop(0)
    print word

def print_last_word(words):
    """print the last word after poping if off"""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


"""
>>> sentence = "All good things come to those who wait."
>>> import less25_module
>>> sentence = "All good things come to those who wait."
>>> words = less25_module.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = less25_module.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> less25_module.print_first_word(sorted_words)
All
>>> less25_module.print_last_word(sorted_words)
who
>>> less25_module.print_first_and_last(sentence)
All
wait.


When should I print vs. return in a function?
You need to understand that print is only for printing to the screen, and that you can actually do both print and return a value. When you understand this then you'll see that the question is kind of a pointless question. You use print when you want to print. You use return when you want to return.
"""
