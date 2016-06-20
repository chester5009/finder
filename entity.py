# -*- coding: utf-8 -*-

import sys, urllib, requests
import time
from PyQt4.QtGui import QTableWidgetItem

class Entity:

    def __init__(self, url, phrase, inteval):
        self.__url = url
        self.__phrase = phrase
        self.__interval = inteval
        self.set_is_found(False)
        self.set_time(0)
    
    def update(self):
        if self.get_time() > self.get_inteval():
            self.set_time(0)
        pass
    
    def get_url(self):
        return self.__url


    def get_phrase(self):
        return self.__phrase


    def get_interval(self):
        return self.__interval


    def get_is_found(self):
        return self.__isFound


    def get_time(self):
        return self.__time


    def set_url(self, value):
        self.__url = value


    def set_phrase(self, value):
        self.__phrase = value


    def set_interval(self, value):
        self.__interval = value


    def set_is_found(self, value):
        self.__isFound = value


    def set_time(self, value):
        self.__time = value
        
    def isFound(self):
        try:
            url = self.get_url()
            sait = urllib.urlopen(url)
    
            whatfound = self.get_phrase()
            
            '''
            f = open("index.html", 'w')
            '''
            data = sait.read()
            print data
            result = data.find(whatfound)
            print result
            #f.write(data)
            #f.close()
            if(result > 0): return True
            else: return False
        except:
            print "Ошибка"
            return False
        pass


    
