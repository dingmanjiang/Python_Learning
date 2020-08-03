"""
There are some standard code for open a url
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# --------------------------------------------------------------------------------
def open_url(url):
    """
    This function is to open a url
    :param url: the target url address
    :return: when it open successfully, it will return the request object. otherwise, return None.
    """

    # try to open url
    try:
        html = urlopen(url, timeout=30)
    except HTTPError:
        return None

    return html
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
def get_bs_object(url_request):
    """
    This function is to get the bs4 object of url
    :param url_request: the object of target url address
    :return: when it get the object, it will return it and otherwise, it will return None.
    """

    # try to get title
    try:
        bs = BeautifulSoup(url_request.read(), 'html.parser')
    except AttributeError:
        return None

    return bs
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
def open_get_bs(url):
    """
    This function is to get the object of bs4 BeautifulSoup.
    :param url: the target url address
    :return: when it get the object, it will return it and otherwise, it will return None.
    """

    # try to open url
    try:
        html = urlopen(url, timeout=30)
    except HTTPError:
        print('can not connect to the web')
        return None

    # try to get the web html string
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
    except AttributeError:
        print('can not parse the request object')
        return None

    # print(bs)
    return bs
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
if __name__ == '__main__':
    url = 'http://www.pythonscraping.com/pages/page1.html'

    url_request = open_url(url)
    if url_request == None:
        print('The web can not open')
        exit()

    title = get_title(url_request)
    if title == None:
        print("Title could not be found")
        exit()
    else:
        print(title)
