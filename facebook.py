#coding:utf-8
import requests
import re

#需求翻墙和请求头
def a():
    header = {
        'Host': "www.facebook.com",
        'User - Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        'Accept - Language': "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        'Accept - Encoding': "gzip, deflate, br",
        'Referer': "https://www.facebook.com/login.php?login_attempt=1&lwv=110",
        'Cookie': "fr=0k2Ax4CCjk8Kjcrds.AWX-cMet5hWKvZj6KLpTZDy1gEE.BXjKcD.nF.AAA.1.0.BXjKeR.AWUrGiBu; datr=A6eMV-JPdln0NDiJpfyFKrlH; sb=dqeMV2pzS_Pe7wTsHP7R3idl; c_user=100011092693900; xs=224%3AVID96AdeNr28PA%3A2%3A1468835702%3A12176; csm=2; s=Aa4NxMKn-PPyaCca.BXjKd2; pl=n; lu=gQgzhjIIzFOgUAvrQ2IKgu5w; p=-2; presence=EDvF3EtimeF1468835731EuserFA21B11092693900A2EstateFDt2F_5b_5dElm2FnullEuct2F1468835103BEtrFnullEtwF3399178164EatF1468835729022G468835731236CEchFDp_5f1B11092693900F2CC; wd=1429x429",
        'Connection': "keep-alive",
        'Cache - Control': "max-age=0"

    }
    url = "https://www.facebook.com/OneRepublic"
    r = requests.get(url,headers=header)
    b = re.search(r'videoData:(.*?]}])', r.text).group(1)
    print b

if __name__ == '__main__':
    a()