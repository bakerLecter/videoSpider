#coding:utf-8
import requests
import re

def a():
    url = "https://vine.co/v/iEeU3VE5iP0"
    r = requests.get(url)
    b = re.search(r'"contentUrl" : "(.*?)",',r.text).group(1)
    print b

if __name__ == '__main__':
    a()
