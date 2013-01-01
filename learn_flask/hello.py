#!/usr/bin/python
# -*- coding: utf-8 -*- 
#****************************************************************#
# ScriptName: hello.py
# Author: root@163.com
# Create Date: 2012-12-31 20:26
# Modify Author: root@163.com
# Modify Date: 2012-12-31 20:26
# Function: 
#***************************************************************#

from flask import Flask
app = Flask(__name__)

#路径最后多一条斜杠比较保险，避免404
@app.route('/hello/')
def hello_word():
    return 'Hello World!!!'

#variable
@app.route('/login/<username>')
def return_username(username):
    return 'welcome, %s' % username

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
