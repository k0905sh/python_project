#이게 실제로 스크래핑 할떄 가장 많이 사용된다 !!!!!!!!!!!!!!!!
#css 선택자를 사용하는 것이 가장 좋은 방식이야 ㅜ#
#https://www.w3schools.com/cssref/trysel.asp
from bs4 import BeautifulSoup
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


html = """
<html><body>
<div id="main">
  <h1>강의목록</h1>
  <ul class="lecs">
    <li>Java 초고수 되기</li>
    <li>파이썬 기초 프로그래밍</li>
    <li>파이썬 머신러닝 프로그래밍</li>
    <li>안드로이드 블루투스 프로그래밍</li>
  </ul>
</div>
</body></html>
"""

soup=BeautifulSoup(html,"html.parser")


h1 = soup.select("div#main > h1")#()안에 들어가는게 css selector
#div태그중에 id가 메인이고 거기의 하위 태그중에 h1태그를 담아와라
print(h1,type(h1))#이녀석은 스트링으로 결과가 나온다!!!

#그래서 반복문을 돌려서
#이런식으로 뽑아주거나
for i in h1:
    print(i.string)


#그래서 이런식으로 하면 1개만 스트링으로 뽑아낼 수 있긴하지
#하나만 뽑아내는 거면 이런식으로 하면 되게ㅐㅆ.
h1=soup.select_one("div#main>h1")
print(h1.string)

list_li =soup.select("div#main>ul.lecs >li")#이거 띄어쓰기 주의 띄어쓰기 하면 값 안나옴!!!
for i in list_li:
    print(i.string)
