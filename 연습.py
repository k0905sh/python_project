import sys
import io
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url='https://www.google.com/search?q=google&sxsrf=ACYBGNTlnFapNE3Ta5jCaCZjYlynu1Gkog:1575367255789&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiu5a-tnJnmAhWLLqYKHem0AAQQ_AUoAnoECA8QBA&biw=958&bih=959'
res=urllib.request.urlopen(url).read()
