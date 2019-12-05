#HttpResponse
#Get방식으로 어떤 api를 사이트에 요청하고 받아와서 출력
"""
웹 API는 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해
 정의된 명세를 일컫는다. 예를 들어 블로그 API를 이용하면 블로그에 접속하지 않고도
 다른 방법으로 글을 올릴 수 있다. 그 외에 우체국의 우편번호 API, 구글과
  네이버의 지도 API등 유용한 API들이 많으므로, 요즘은 홈페이지 구축이나
   추가개편 시 따로
 추가로 개발하지 않고 이런 오픈 API를 가져와 사용하는 추세다.
"""

import sys
import io
import urllib.request
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API="https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"
#이사이트에서 요구하는 형식대로 만들어 주기 위한 작업을 하는 거임 지금
"""
$ curl 'https://api.ipify.org?format=json'
{"ip":"14.39.169.213"}
"""
values =dict(
    ctxCd = '1001'
)

print(values)
params = urlencode(values)#원하는 형식으로 바꿔주기 위해서..... 사용
print('after',params)

url=API+"?"+params
print(url)

reqData = urllib.request.urlopen(url).read().decode("utf-8")
print(reqData)
