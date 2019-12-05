from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

savePath ="C:\\imagedown\\"
base = "https://www.inflearn.com/"
quote = rep.quote_plus("異붿쿇-媛뺤쥖")

url = base + quote

res = req.urlopen(url).read()

soup = BeautifulSoup(res,"html.parser")

recommand = soup.select("ul.slides")[0]

try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise


for i,e in enumerate(recommand,1):
    with open(savePath+"title_"+str(i)+".txt", "wt") as f:
        f.write(e.select_one("h4.block_title > a ").string)
    fullfilename = os.path.join(savePath, savePath+'img_'+str(i)+'.png')
    req.urlretrieve(e.select_one("div.block_media > a > img")['src'],fullfilename)

print("媛뺤쥖 ?뺣낫 ?띿뒪??異쒕젰 諛??대?吏 ?ㅼ슫 ?꾨즺!")
