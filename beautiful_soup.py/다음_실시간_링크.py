from bs4 import BeautifulSoup
import urllib.request

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url="https://www.daum.net/"
res = urllib.request.urlopen(url).read()
soup = BeautifulSoup(res,"html.parser")

data =soup.select("div.realtime_part>ol.list_hotissue.issue_row>li")


print(data)
print('------------------------------------')
print('------------------------------------')
print('------------------------------------')
print('------------------------------------')



for i,j in enumerate(data,1):
    print(i,j.find("a").string,j.find("href"),j["href"])
