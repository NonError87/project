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

url = "https://bing.ioliu.cn"

def setWallpaper(bmp):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, bmp)
    
def geturl(url):
    L = []
    soup = BeautifulSoup(request.urlopen(request.Request(url)).read(), "html5lib")
    for link in soup.find_all('a'):
        r = str(link.get('href'))
        m = re.match(r"(/photo/)(.+)(\?.+)(download)", r)
        if m:
            realurl = url + r
            return realurl, m.groups()[1]
        
def createBMP(url, img):
    request.urlretrieve(url, img+".jpg")
    im = Image.open(img+".jpg").save(img+".bmp", quality = 100)
    os.remove(img+".jpg")
    return img+".bmp"
    
def main(url):
    while True:
        try:
            c = geturl(url)
            bmp = createBMP(c[0], c[1])
            setWallpaper(bmp)
            break
        except:time.sleep(60)

if __name__ == '__main__':
        try:main(url)
