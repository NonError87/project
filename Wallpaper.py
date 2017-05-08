# -*- coding:utf-8 -*-

import os
import re
import win32api
import win32con
import win32gui
from random import choice
from urllib import request

import html5lib
from PIL import Image
from bs4 import BeautifulSoup

url = "https://bing.ioliu.cn/"

def setWallpaper(bmp):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, bmp)
    
def geturl(url):
    L = []
    soup = str(BeautifulSoup(request.urlopen(request.Request(url)).read(), "html5lib").find('img').get('src'))
    realurl = re.sub(r"thumbnail", "large", soup)
    r = re.match(r"(https://wx1.sinaimg.cn/large/)(.+)(\.jpg)", realurl).groups()[1]
    return realurl, r
        
def createBMP(url, img):
    request.urlretrieve(url, "./pics"+img+".jpg")
    Image.open("./pics"+img+".jpg").save("./pics"+img+".bmp")
    os.remove("./pics"+img+".jpg")
    return "./pics"+img+".bmp"
    
def main(url):
    c = geturl(url)
    bmp = createBMP(c[0], c[1])
    setWallpaper(bmp)
    
if __name__ == '__main__':
    main(url)