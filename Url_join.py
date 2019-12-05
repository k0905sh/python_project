from urllib.parse import urljoin

baseUrl ="http://test.com/html/a.html"
print(">>", urljoin(baseUrl,"b.html"))
print(">>", urljoin(baseUrl,"sub/b.html"))
print(">>", urljoin(baseUrl,"../b.html"))#한 디렉토리 올라간다음 b.html
print(">>", urljoin(baseUrl,"../img/img.jpg"))
#url경로를 지정하면 절대 경로는 지정해 놓고 나머지 파일들만 위치를 지정해 줄 수 있다.
