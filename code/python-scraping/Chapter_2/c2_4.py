
import openURL
import re

url = 'http://www.pythonscraping.com/pages/page3.html'
html = openURL.open_url(url)
if html == None:
    print('The web can not be connected.')
    exit()

bsObj = openURL.get_bs_object(html)
if bsObj == None:
    print('Can not get the web bs object')
    exit()

images = bsObj.findAll('img', {'src': re.compile(r'..\/img\/gifts\/img\d+.jpg')})
for image in images:
    print(image['src'])

