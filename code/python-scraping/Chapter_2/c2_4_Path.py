import sys, re
BASE_DIR = '/home/kevin/eclipse-workspace/Python_Learning/code/'
sys.path.append(BASE_DIR)

from mybible import openURL

url = 'http://www.pythonscraping.com/pages/page3.html'

bsObj = openURL.open_get_bs(url)
if bsObj == None:
    print('Can not get the web bs object')
    exit()

images = bsObj.findAll('img', {'src': re.compile(r'..\/img\/gifts\/img\d+.jpg')})
for image in images:
    print(image['src'])

