# coding:utf-8
import requests
import re


def a():
    url = "http://www.funnyordie.com/videos/6f7876c5d8/munchies-with-toni-charlene-jonathan-van-ness?_cc=__m___&_ccid=e7160e6d-06fb-40f9-af2c-c5694c154fa1"
    r = requests.get(url)
    b = re.search(r'<source src="(.*?.mp4)',r.text).group(1)
    print b
if __name__ == '__main__':
    a()
