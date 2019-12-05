import sys
import io
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


imgUrl ="http://blogfiles.naver.net/20140413_184/moisophiaj_1397389104586LN5Bi_JPEG/%B1%CD%BF%A9%BF%EE_%B5%BF%B9%B0_%BB%E7%C1%F8_%2810%29.jpg"
htmlUrl ="https://google.com"

savePath1="c:/section2/test.jpg"#세이브 페스에 경로 뿐만 아니라 파일 이름 까지 지정해 줘야함
savePath2="c:/section2/index.html"

f=urllib.request.urlopen(imgUrl).read()
f2=urllib.request.urlopen(htmlUrl).read()

saveFile1=open(savePath1,'wb')#w:Write r:Read a:Add
saveFile1.write(f)
saveFile1.close()

with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)


print("다운로드 완료")

#urlopen vs urlretrieve
# urlretrieve:
# 바로 다이렉트로 다운받는다 저장->오픈->변수에 할당->파싱->저장
# 여러 데이터를 쭉쭉 한번에 다운 받아야 할때는 이걸 주로 쓴다 왜냐
#변수 지정이 필요가 없으니ㅏ까

# urlopen:
# 저장을 하기전에 변수를 할당을 하고 with구문들을 통해 저장
