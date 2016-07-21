# coding:utf-8
import requests
import re
import json
import urlparse


def a():
    url = "https://vimeo.com/channels/staffpicks/174158118"
    r = requests.get(url)
    video_url = re.search(r'video:url" content="(.*?)"', r.text).group(1)#

    r2 = requests.get(video_url)

    b = re.search(r'"progressive":(.*?])},',r2.text).group(1)
    b = b[1:-2].split(',')#把字符串格式的list[]转换为真正的list[]
    print b

if __name__ == '__main__':
    a()
