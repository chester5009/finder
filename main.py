# -*- coding: utf-8 -*-

import sys,urllib,requests
import time
import Py

sait=urllib.urlopen("http://forum.ubuntu.ru/index.php?topic=231908.0")

whatfound="поверь мне, все есть в репозиториях Kubuntu"

f=open("index.html",'w')
data=sait.read()
print data
print data.find(whatfound)
f.write(data)
f.close()

