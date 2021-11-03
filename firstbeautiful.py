from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml


html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
bx = BeautifulSoup(html.read(), 'lxml')
print(bs.h1)
print('--------------------------------')
print(bs)
print('--------------------------------')
print(bx)