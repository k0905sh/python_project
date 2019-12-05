from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import sys
import io
import os#operation system 명령어 사용 가능

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quoto = urllib.parse.quote_plus("아이유")
url = base + quoto
res=urllib.request.urlopen(url)
savePath="C:\\Section2\\img\\"

try:#이건 만약 저장폴더가 없을시 폴더를 만들어 주는 것임
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))

except OSError() as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패")
        raise

soup=BeautifulSoup(res,"html.parser")
img_list=soup.select("div.img_area > a.thumb._thumb > img")
print(img_list)

for i, img_list in enumerate(img_list,1):
    # print(img_list['src'])
#근데 이렇게 뽑아 datasource값은 스트림 값으로들어가
#왜냐하면 user-agent 값이 없기 때문이지
#파이썬을통해 http통신을 하니까



    # print(img_list['data-source']) #이게 실직적으로 이미지 파일 다운 받는 경로
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')#이렇게 해줘야지 실직적인
    print(fullFileName)
    urllib.request.urlretrieve(img_list['data-source'],fullFileName)

print('다운완료')
