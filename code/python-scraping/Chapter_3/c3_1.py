import sys, re, datetime, random
BASE_DIR = '/home/kevin/eclipse-workspace/Python_Learning/code/'
sys.path.append(BASE_DIR)

from mybible import openURL

# set the proxy server
import socks
import socket
socks.set_default_proxy(socks.SOCKS5, 'localhost', 1080)
socket.socket = socks.socksocket

url = 'http://en.wikipedia.org'
random.seed(datetime.datetime.now())

def getLink(articleUrl):
    bsObj = openURL.open_get_bs(url+articleUrl)
    if bsObj == None:
        print('Can not get the web bs object')
        exit()

    return bsObj.find('div', {'id':'bodyContent'}).findAll('a', href = re.compile(r'^(/wiki/)((?!:).)*$'))

links = getLink('/wiki/Kevin_Bacon')
while len(links) >0:
    newArticle = links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    links = getLink(newArticle)