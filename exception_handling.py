# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

# import urllib.request
# import urllib.error
#
# try:
#     urllib.request.urlopen("https://blog.csdn.net")
#     print("text")
# except urllib.error.URLError as e:
#     if hasattr(e, "code"):
#         print(e.code)
#     if hasattr(e, "reason"):
#         print(e.reason)

# 浏览伪装
import urllib.request
import os

url = "http://blog.csdn.net"
headers = ("User_Agent",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
date = opener.open(url).read()
filename = "D:\爬虫练习\erorr.html"
# if not os.path.exists(filename):
#     file = open(filename, "wb")
#     file.write(date)
#     file.close()
# else:
#     file = open(filename, "wb")
#     file.write(date)
#     file.close()
file = open(filename, "wb")
file.write(date)
file.close()