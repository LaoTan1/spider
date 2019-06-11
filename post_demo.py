# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

import urllib.request
import urllib.parse

url = "https://www.iqianyue.com/mypost/"
postdate = urllib.parse.urlencode({
    "name": "laotan",
    "poss": "laotan",
}).encode("utf-8")
req = urllib.request.Request(url, postdate)
ret = urllib.request.urlopen(req).read().decode("utf-8")

