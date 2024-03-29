from bs4 import BeautifulSoup
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#html 파일 내용
#이번예제는 html변수가 아니라 파일을 읽어와서 하는 것임
"""
<html>
<body>
<div id="foods">
  <h1>안주 및 주류</h1>
  <ul id="fd-list">
    <li class="food hot" data-lo="ko">닭도리탕</li>
    <li class="food" data-lo="jp">돈까스</li>
    <li class="food hot" data-lo="ko">삼겹살</li>
    <li class="food" data-lo="us">스테이크</li>
  </ul>
  <ul id="ac-list">
    <li class="alcohol" data-lo="ko">소주</li>
    <li class="alcohol" data-lo="us">맥주</li>
    <li class="alcohol" data-lo="ko">막걸리</li>
    <li class="alcohol high" data-lo="cn">양주</li>
    <li class="alcohol" data-lo="ko">동동주</li>
  </ul>
</div>
<body>
</html>
"""

fp=open("food-list.html",encoding='utf-8')
soup = BeautifulSoup(fp,'html.parser')

print("1",soup.select_one("li:nth-of-type(8)").string)
