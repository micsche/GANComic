#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import re
import sys
import os
import http.cookiejar
import json
import urllib.request, urllib.error, urllib.parse

def get_soup(url,header):
    #return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),
    # 'html.parser')
    return BeautifulSoup(urllib.request.urlopen(
        urllib.request.Request(url,headers=header)),
        'html.parser')

query = sys.argv[1]
url="https://www.bing.com/images/search?q="+query+"%20Pen%20and%20Ink%20Drawings&qs=n&form=QBIR&qft=%20filterui%3Acolor2-bw%20filterui%3Aphoto-linedrawing&sp=-1&pq=pirate%20pen%20and%20ink%20drawings&sc=0-27&cvid=E2D347DE3AF547EF967728A400B7B3DE&first=1&scenario=ImageBasicHover"
print(url)

#add the directory for your image here
DIR="Pictures"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
soup = get_soup(url,header)

ActualImages=[]# contains the link for Large original images, type of  image
for a in soup.find_all("a",{"class":"iusc"}):
    #print a
    # mad = json.loads(a["mad"])
    # turl = mad["turl"]
    m = json.loads(a["m"])
    murl = m["murl"]
    turl = m["turl"]

    image_name = urllib.parse.urlsplit(murl).path.split("/")[-1]
    print(image_name)

    ActualImages.append((image_name, turl, murl))

print("there are total" , len(ActualImages),"images")

if not os.path.exists(DIR):
    os.mkdir(DIR)

DIR = os.path.join(DIR, query.split()[0])
if not os.path.exists(DIR):
    os.mkdir(DIR)

cnt = 0
##print images
for i, (image_name, turl, murl) in enumerate(ActualImages):
    try:
        #req = urllib2.Request(turl, headers={'User-Agent' : header})
        #raw_img = urllib2.urlopen(req).read()
        #req = urllib.request.Request(turl, headers={'User-Agent' : header})
        raw_img = urllib.request.urlopen(turl).read()

        cntr = len([i for i in os.listdir(DIR) if image_name in i]) + 1
        #print cntr
        cnt = cnt + 1
        f = open(os.path.join(DIR, str(cnt)+image_name), 'wb')
        f.write(raw_img)
        f.close()
    except Exception as e:
        print("could not load : " + image_name)
        print(e)
