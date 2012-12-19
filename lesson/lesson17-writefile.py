#!/usr/bin/python
#-*- coding:utf-8 -*-
# ScriptName: lesson17-writefile.py

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Coping from %s to %s" % (from_file, to_file)

indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %s" % exists(to_file)
print "Ready, hit RETURN to continue,CTRL-C to abort."
raw_input()    #给用户一个确定的机会

out_file = open(to_file,'w')
out_file.write(indata)

print "Alright, all done."
out_file.close()



"""
#./lesson17-writefile.py example.txt to_file
Coping from example.txt to to_file
The input file is 30 bytes long
Does the output file exist? False         #被写入的文件可以不存在
Ready, hit RETURN to continue,CTRL-C to abort.

Alright, all done.
"""
