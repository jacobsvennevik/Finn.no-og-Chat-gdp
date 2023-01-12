from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)

    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

def try_one_more(body):
    fasiliteter = []
    Nøkkelinfo_dict = {}
    text = []
    
    soup = BeautifulSoup(body, 'html.parser')

html = urllib.request.urlopen('https://www.finn.no/realestate/lettings/ad.html?finnkode=287010242').read()
print(text_from_html(html))

