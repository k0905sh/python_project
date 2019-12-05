from bs4 import BeautifulSoup
import urllib.request

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url="https://www.inflearn.com/"
res= urllib.request.urlopen(url).read()
soup = BeautifulSoup(res,"html.parser")




data=soup.select(".columns.is-mobile.courses_card_list_body ")[0]
######클래스 내부에 띄어쓰기 가 되어있는경우 . 을 찍으준다

print(data)
