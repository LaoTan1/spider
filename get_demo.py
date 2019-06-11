# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

import urllib.request
import re

keywd = "京东"
keywd = urllib.request.quote(keywd)
for i in range(1, 20):
    url = "http://www.baidu.com/s?wd=" + keywd + "&pn=" + str((i - 1) * 10)
    date = urllib.request.urlopen(url).read().decode("utf-8")
    pat1 = "title:'(.*?)',"
    pat2 = 'title:"(.*?)",'
    rst1 = re.compile(pat1).findall(date)
    rst2 = re.compile(pat2).findall(date)
    for j in range(0, len(rst1)):
        print(rst1)
    for j in range(0, len(rst2)):
        print(rst2)
