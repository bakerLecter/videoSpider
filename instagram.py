#coding:utf-8
import requests
import re

def a():
    url = "https://www.instagram.com/p/BH2RqvSg-iP/"
    r = requests.get(url)
    b = re.search(r'<meta property="og:video" content="(.*?)"',r.text).group(1)
    print b

if __name__ == '__main__':
    a()