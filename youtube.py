# coding:utf-8
import requests
import re
import json
import urlparse



def a():
    url = "https://www.youtube.com/watch?v=5yAU52qfYuU"
    r = requests.get(url)
    html = r.text
    try:
        args = re.search(r'"args":({.*?})', html).group(1)#正则获取 "args":{}里面的数据
        url_json = json.loads(args)#转换为json
        video_dict = urlparse.parse_qs(url_json['url_encoded_fmt_stream_map'])#url解码
        print json.dumps(video_dict, indent=4)
    except:
        pass


if __name__ == '__main__':
    a()