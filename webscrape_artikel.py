import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from bs4.element import Comment

print('pang')


def get_html(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    return soup


def add_links():
    urls = []
    for i in range(100):
        if i == 0:
            url = f'https://www.finn.no/realestate/homes/search.html?location=0.0.20061&sort=PUBLISHED_DESC'
        else:
            url = f'https://www.finn.no/realestate/homes/search.html?location=0.20061&page={i}&sort=PUBLISHED_DESC'
        soup = get_html(url)
        urls.extend(links_on_page(soup)) 
        if len(urls) > 1000:
            return urls
        sleep(randint(2,30))
    return urls

def links_on_page(s):
    urls = []
    for link in s.find_all('a', class_="link link--dark sf-ad-link sf-realestate-heading" ):
        raw = link.get('href')
        if "homes" in raw:
            urls.append(raw)
    return urls

urls = []
with open('urls.txt') as f:
    content = f.readlines()
    for line in content:
        if not line:
            break
        urls.append(line.strip())

def find_fas(url, tag, name):
    soup = get_html(url)
    tekst = []
    for t in soup.find_all(tag, class_= name):
        tekst.append(t.text)
    return tekst

def find_el(url, tag, name):
    soup = get_html(url)
    return soup.find(tag, class_= name).text

def scrape_stats(url):
    soup = get_html(url)
    stats_dict = dict()
    stats = soup.find("dl", class_="grid md:grid-cols-3 grid-cols-2 pb-8 gap-16 m-0")
    stats_val = stats.find_all('dd')
    stats_key = stats.find_all('dt')
    
    for i in range(len(stats) - 1):
        stats_dict[stats_key[i].text] = stats_val[i].text

    return stats_dict


for i in range(10):
   #print(find_el(urls[i], "div", "pt-16 sm:pt-40"))
   #print(find_fas(urls[i], "div", "py-4 break-words"))
   #print(scrape_stats(urls[i]))
   #print(find_el(urls[i], "span", "pl-4"))





print('pang pang')
        

