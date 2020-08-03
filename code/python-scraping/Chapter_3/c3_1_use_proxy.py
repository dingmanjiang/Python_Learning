import sys, re
BASE_DIR = '/home/kevin/eclipse-workspace/Python_Learning/code/'
sys.path.append(BASE_DIR)

from mybible import openURL

# set the proxy server
import socks
import socket
socks.set_default_proxy(socks.SOCKS5, 'localhost', 1080)
socket.socket = socks.socksocket

url = 'https://www.google.com'

bsObj = openURL.open_get_bs(url)
if bsObj == None:
    print('Can not get the web bs object')
    exit()

print(bsObj)
# images = bsObj.findAll('img', {'src': re.compile(r'..\/img\/gifts\/img\d+.jpg')})
# for image in images:
#     print(image['src'])