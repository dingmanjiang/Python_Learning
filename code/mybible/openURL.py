"""
There are some standard code for open a url
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


# --------------------------------------------------------------------------------
def get_title(url):
    """
    This function is to get the title of url
    :param url: the target url address
    :return: when it get the title, it will return the title string. otherwise, return None.
    """

    # try to open url
    try:
        html = urlopen(url)
    except HTTPError:
        return None

    # try to get title
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title_str = bs.body.h1
    except AttributeError:
        return None

    return title_str


# --------------------------------------------------------------------------------

title = get_title("http://www.pythonscraping.com/pages/page1.html")  # the url is a test website
if title is None:
    print("Title could not be found")
else:
    print(title)
