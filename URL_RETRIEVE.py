import sys
import io
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#방법1 절차대로 이미지 다운로드
imgUrl ="http://blogfiles.naver.net/20140413_184/moisophiaj_1397389104586LN5Bi_JPEG/%B1%CD%BF%A9%BF%EE_%B5%BF%B9%B0_%BB%E7%C1%F8_%2810%29.jpg"
# savePath="c:/section2/test1.jpg"#이미지를 저장할 위치
# urllib.request.urlretrieve(imgUrl,savePath)#첫번째 변수 주소,두번째 변수 저장 위치
# #이걸 실행하면 이미지 다운 하는 것임
# print("complete")


#방법2 URL이용 바로 다운로드
htmlUrl ="https://google.com"
savePath1="c:/section2/test.jpg"#세이브 페스에 경로 뿐만 아니라 파일 이름 까지 지정해 줘야함
savePath2="c:/section2/index.html"

urllib.request.urlretrieve(imgUrl, savePath1)
urllib.request.urlretrieve(htmlUrl, savePath2)

print("다운로드 완료")
