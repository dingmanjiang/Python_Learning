from urllib.request import urlopen
from bs4 import BeautifulSoup
import openURL


url = 'http://www.pythonscraping.com/pages/page3.html'
html = openURL.open_url(url)
if html == None:
    print('Can not open the website')
    exit()

bsObj = BeautifulSoup(html, 'html.parser')

#for child in bsObj.find("table", {"id": "giftList"}).children:
#for child in bsObj.find("table", {"id": "giftList"}).descendants:
#    print(child)

#for sibling in bsObj.find('table', {'id': 'giftList'}).tr.next_siblings:
#    print(sibling)

print(bsObj.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())