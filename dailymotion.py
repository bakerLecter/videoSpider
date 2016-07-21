# coding:utf-8
import requests
import re
import json
import urlparse

def a():
    url = "http://www.dailymotion.com/video/x4k6xcm_summary-stage-12-montpellier-mont-ventoux-tour-de-france-2016_sport"
    r = requests.get(url)
    b = re.search(r'"qualities":(.*?}]}),',r.text).group(1)
    print json.loads(b)


if __name__ == '__main__':
    a()