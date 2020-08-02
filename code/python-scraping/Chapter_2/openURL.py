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
def get_title(url_request):
    """
    This function is to get the title of url
    :param url_request: the object of target url address
    :return: when it get the title, it will return the title string. otherwise, return None.
    """

    # try to get title
    try:
        bs = BeautifulSoup(url_request.read(), 'html.parser')
        title_str = bs.body.h1
    except AttributeError:
        return None

    return title_str
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
