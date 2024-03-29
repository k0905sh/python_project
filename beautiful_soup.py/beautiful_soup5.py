from bs4 import BeautifulSoup
import sys
import io
import re #regular express

#re 로하는 것은 사용률이 많이 떨어짐!!!!

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


html = """
<html><body>
  <ul>
    <li><a id="naver" href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="http://www.KLKK.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html,"html.parser")
print(soup.find(id="naver").string) #li 태그에 id 가 있을 경우

li = soup.find_all(href=re.compile(r"^https://"))#이게 정규 표현식 시작은 https로 한다
print(li)

for e in li:
    print(e.attrs['href'])
