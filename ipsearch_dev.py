#!/usr/bin/python
# -*- coding=utf-8 -*-

#module
import urllib
import json
import os

#Variable
url="http://ip.taobao.com/service/getIpInfo.php?ip="
f = open('ip.txt').readlines()
out_file = open('res_file','w')

#function
def ip_detail():
	data=urllib.urlopen(url+ip).read()
	datadict=json.loads(data)
#    return datadict["data"]["isp"]
	return  datadict["data"]["isp"] + "\n"
#	return u"该IP的详细信息为:\n" + u"国家/地区：" + datadict["data"]["country"] + "/" + datadict["data"]["area"] + u"\n省份：\t" + datadict["data"]["region"] + u"\n城市:\t" + datadict["data"]["city"] + u"\n运营商：" + datadict["data"]["isp"] 
    
#main
if __name__=="__main__":
    for ip in f:
        out_file.write(ip_detail().encode('utf8'))


#	os.system("clear")
 #   for ip in f:
  #      print ip_detail()
