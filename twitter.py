# coding:utf-8
import requests
import re


def a():
    #需要一个头 表明他是手机
    url = "https://mobile.twitter.com/Astro_Jeff/status/754745879345717248/video/1"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }
    r = requests.get(url,headers=header)
    b = re.search(r'"videoUrl":"(.*?)"',r.text).group(1)
    print b


if __name__ == '__main__':
    a()
