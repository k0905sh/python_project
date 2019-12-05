#HttpResponse
#Get방식으로 어떤 api를 사이트에 요청하고 받아와서 출력


import sys
import io
import urllib.request
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

API="https://api.ipify.org"
#이사이트에서 요구하는 형식대로 만들어 주기 위한 작업을 하는 거임 지금
"""
$ curl 'https://api.ipify.org?format=json'
{"ip":"14.39.169.213"}
"""
values =dict(
    format = 'jasonp'
)

print(values)
params = urlencode(values)#원하는 형식으로 바꿔주기 위해서..... 사용
print('after',params)

url=API+"?"+params
print(url)

reqData = urllib.request.urlopen(url).read().decode("utf-8")
print(reqData)
