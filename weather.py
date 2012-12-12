#!/usr/bin/python2.6
# -*- coding=utf-8 -*-

########模块
import urllib
import json
import termcolor
import os

########变量
url="http://weather.china.xappengine.com/api?city="

########类或函数

class GetWeath:
    def __init__(self,url,city):
	self.url = url
	self.city = city
	self.content = urllib.urlopen(self.url+self.city).read()
    	self.detail = json.loads(self.content)

    def weather_type(self,type):
        if type == "wlt":
       	    return self.detail["name"]
        elif type == "text1":
    	    return self.detail["forecasts"][0]["text"]
        elif type == "low1":
	    return str(self.detail["forecasts"][0]["low"])
        elif type == "high1":
	    return str(self.detail["forecasts"][0]["high"])
        elif type == "text2":
	    return self.detail["forecasts"][1]["text"]
        elif type == "low2":
	    return str(self.detail["forecasts"][1]["low"])
        elif type == "high2":
	    return str(self.detail["forecasts"][1]["high"])
        else:
	    pass

if __name__ == '__main__':
    os.system("clear")
    city=raw_input("请输入要查询的城市（拼音）：")
    wea_message = GetWeath(url,city)
    name = wea_message.weather_type('wlt')
    text1 = wea_message.weather_type('text1')
    low1 = wea_message.weather_type('low1')
    high1 = wea_message.weather_type('high1')
    text2 = wea_message.weather_type('text2')
    low2 = wea_message.weather_type('low1')
    high2 = wea_message.weather_type('high2')
    try:
	print u"你要查询的城市：" + termcolor.colored(name,'yellow', attrs=['bold']) + \
		u"\n\n今日天气：\n" + text1 + u"\n最低温：" + low1 + u"\n最高温：" + \
		high1 + u"\n\n明天天气：\n" + text2 + u"\n最低温：" + low2 + u"\n最高温：" + high2
    except:
	print termcolor.colored("Input error!!!",'red',attrs=['bold'])
