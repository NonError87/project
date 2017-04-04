# -*- coding: utf-8 -*-
 
from urllib import request
from bs4 import BeautifulSoup
import re
import html5lib
import os
from time import ctime
from concurrent import futures

url = input("url:")

headers = ({
'Connection': 'Keep-Alive',
'Accept': 'text/html, application/xhtml+xml, */*',
'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})

if not os.path.exists("Pictures"):
    os.mkdir("Pictures")
print("start", "at", ctime())
    
def soup(url, headers, r):
    l = []
    req = request.Request(url, headers=headers)
    soup = BeautifulSoup(request.urlopen(req).read(), "html5lib")
    for link in soup.find_all("a"):
        if re.match(r, str(link.get('href'))):
            if re.match(r + r"(/?re)", str(link.get('href'))):pass
            else:l.append(link.get('href'))
    return list(set(l))

def downpic(pic, headers):
    req = request.Request(pic, headers=headers)
    soup = BeautifulSoup(request.urlopen(req).read(), "html5lib")
    for link in soup.find_all(id="img"):
        Pic = link.get("src")
    r = re.split(r'/', Pic)
    path = "./Pictures/" + r[-1]
    with open(path, "wb", 100)as f:
        f.write(request.urlopen(Pic).read())

def start(url, headers):
    souping = soup(url, headers, r"(.+)(/g/)(.+)")
    print("start to translate", "at", ctime())
    n = 1
    for urls in souping:
        pics.append(soup(urls, headers, r"(.+)(/s/)(.+)"))
        print("Traversal", n, "/", len(souping), "at", ctime())
        n += 1
    return pics

def main(urls):
    m = 1
    with futures.ThreadPoolExecutor(max_workers = 20) as executor:
        future = [executor.submit(downpic, url, headers) for url in urls]
        for future in futures.as_completed(future):
            print(m, "/", len(urls), "at", ctime())
            m += 1
            
if __name__ == '__main__':
    pics = []
    urls = []
    for pics in start(url, headers):
        for pic in pics:
            urls.append(pic)
    main(urls)
    print("all DONE", "at", ctime())
