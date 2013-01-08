#!/usr/bin/python
#-*- coding:utf-8 -*-
#***************************************************************#
# Author: root@163.com
# Create Date: 2013-01-08 15:52
# Modify Author: root@163.com
# Modify Date: 2013-01-08 15:52
# Function: 
# ScriptName: searchip.py
#***************************************************************#

#!/usr/bin/python
# -*- coding=utf-8 -*-

#module
import urllib
import json
import os
import termcolor

#Variable
url="http://ip.taobao.com/service/getIpInfo.php?ip="

#function
def ip_detail():
        data=urllib.urlopen(url+ip).read()
        datadict=json.loads(data)
        return u"该IP的详细信息为:\n" + u"国家/地区：" + datadict["data"]["country"] + "/" + datadict["data"]["area"] + u"\n省份：\t" + datadict["data"]["region"] + u"\n城市:\t" + datadict["data"]["city"] + u"\n运营商：" + datadict["data"]["isp"] 


#main
if __name__=="__main__":
    os.system("clear")
    ip=raw_input("input ip address>")
    print ip_detail()
