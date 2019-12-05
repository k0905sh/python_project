from bs4 import BeautifulSoup
import urllib.request
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url="https://finance.naver.com/sise/sise_quant.nhn"
res = urllib.request.urlopen(url).read()#이거

soup = BeautifulSoup(res,"html.parser")
# print(soup.prettify())

#####tag.classname#######
#####tag#id########
data=soup.select("table.type_2>tr")

for i,j in enumerate(data):
    if j.find("a") is not None:#이거 작업 안해주면 스트링으로 나오지 않음
        print(i,j.find("a").string)#a태그의 스트링값만 <a>string<a>
