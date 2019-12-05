from bs4 import BeautifulSoup
import sys
import io
#직접접근으로 태그 가져오기

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html ="""
<html>
<body>
<h1>파이썬 비티퓰수프 공부</h1>
<p>태그 선택자</p>
<p>css선택자</p>
</body>
</html>
"""

print(html)

soup = BeautifulSoup(html,'html.parser' )#(url,parser 지정)
print('soup',type(soup))

print('preetyfly',soup.prettify())#자동으로 들여쓰기 해주는 기능이있다


h1=soup.html.body.h1
print(h1,type(h1))
print(h1.string,type(h1.string))

p1=soup.html.body.p
print('p1',p1.string)

p2=p1.next_sibling#한번만 이동하면 \n 이게 찍히는 거.
print(p2.string)

p3=p1.previous_sibling.previous_sibling
print(p3.string)
