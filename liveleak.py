# coding:utf-8
import requests
import re


def a():
    url = "http://m.liveleak.com/view?i=05a_1468858394"
    header = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
    }
    r = requests.get(url)#, headers=header)
    b = re.search(r'file: "(.*?)",',r.text).group(1)
    print b

if __name__ == '__main__':
    a()