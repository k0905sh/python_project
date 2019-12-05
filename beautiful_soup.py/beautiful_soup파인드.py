from bs4 import BeautifulSoup
import sys
import io
#find_all, find위주!!!
#근데 이런 방식은 좋지 않은것이다.
#html양이 많아지면 유지 보수가 겁나게 힘들기 때문이지
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="http://www.KLKK.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup= BeautifulSoup(html,"html.parser")
#url주소를 연속으로 가져와서 파싱을 해볼깨
#그러러면 url코드를 한번에 가져오는게 좋겠지

links = soup.find_all("a")#soup.find_all(tag)

a=soup.find_all("a",string="daum")#스트링이 다음인 노드만 가져온다
#가져오는데 근데!!!! <tag>daum<tag> 이렇게 되있는 daum만 가져옴
c=soup.find_all("a",limit=3)
b=soup.find("a")#이건a태그 맨 위에 있는 거만
d=soup.find_all(string=["naver","google"])#태그가 아니라 text를 가져온#ㅑ


print("find_all-->",a)
print("find-->",b)
print("find_all.limit-->",c)
print("find_all.string-->",d)

#
# for a in links:
#     print('a==>',a)
#     href = a.attrs['href'] #a라는 변수에 herf태그가 붙은 것들을 저장한다
#     txt=a.string#이거 중요하다 이제 좀 외우자 a.string이거 하면 tag에 담긴text만 나오ㅓㅁ
#     print('txt=>',txt ,'href=>',href)
