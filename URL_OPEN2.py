#HttpResponse
#Get

import sys
import io
import urllib.request
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url ="https://www.naver.com/"
mem = urllib.request.urlopen(url)
print(type(mem))

# print("getUrl->",mem.geturl())
# print("status->",mem.status)#200,404,403,500(정산,없음,접속 거절,서버자체 에러)
# print("headers->",mem.getheaders())

#이 위에 있는 3가지 모두 info 한번 돌리면 전부 확인 가능
# print("info-->",mem.info())
# print("code-->",mem.getcode())
# print("read-->",mem.read(50))# read 안에 숫자를 넣으면 해당 바이트 만큼 리소스를 가져온다
# print("read-->",mem.read(50).decode("utf-8"))# 이러면 디코딩을 해서 가져올 수 있다!! 이걸 좀더 많이 씀
#

print(urlparse("https://www.naver.com"))#url을 파싱해 주는 친구임!
