from bs4 import BeautifulSoup
import urllib.request
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url='https://finance.naver.com/'
res=urllib.request.urlopen(url).read()
soup = BeautifulSoup(res,"html.parser")

# print("soup",soup.prettify())#이건 그냥 코드를 가독성 좋게 보여주는것 .prettify
print()

top=soup.select("tbody#_topItems1 > tr.up")
#태그.class or 태그#id
# print(top)
print()

for i,j in enumerate(top):
    print(i+1,">",j.find("a"),j.find("td").string)#아직 파싱이 덜된거야 아직 이건 clss의 인스턴스이기 때문이지

#url데이터 ->파싱(BeautifulSoup) ->find("여기 안에는 태그명이 들어간")
