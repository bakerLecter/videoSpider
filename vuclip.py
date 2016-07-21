#coding:utf-8
import requests
import re

def a():
    url = "http://vuclip.tv/video/2vjPBrBU-TM/sia-chandelier-official-video.html"
    r = requests.get(url)
    b = re.search(r'source src="(.*?)"',r.text).group(1)
    print b

if __name__ == '__main__':
    a()