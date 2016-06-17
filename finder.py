# -*- coding: utf-8 -*-

import sys, urllib, requests
import time
from PyQt4.QtGui import QTableWidgetItem

class Finder:
    
    
    
    def __init__(self):
        pass

    def get_url(self):
        return self.__url


    def get_phrase(self):
        return self.__phrase


    def get_interval(self):
        return self.__interval


    def set_url(self, value):
        self.__url = value


    def set_phrase(self, value):
        self.__phrase = value


    def set_interval(self, value):
        self.__interval = value
        
    def isFound(self):
        try:
            url="http://www.porn.com/videos/blonde-with-huge-tits-fucks-a-man-with-huge-muscles-2506969"
            sait = urllib.urlopen(url)
    
            whatfound = self.__phrase
            
            f = open("index.html", 'w')
            data = sait.read()
            print data
            result=data.find(whatfound)
            print result
            f.write(data)
            f.close()
            if(result>0): return True
            else: return False
        except:
            print "Ошибка"
            return False
        pass
    
    

    
    
    
    pass
    url = property(get_url, set_url, None, None)
    phrase = property(get_phrase, set_phrase, None, None)
    interval = property(get_interval, set_interval, None, None)
