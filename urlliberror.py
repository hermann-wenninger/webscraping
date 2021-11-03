from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as BS

def getTitle(url):
    html = urlopen(url)
    bsx = BS(html.read(), 'html.parser')
    title = bsx.body.h1
    print(title)

getTitle('http://www.pythonscraping.com/pages/page1.html')

