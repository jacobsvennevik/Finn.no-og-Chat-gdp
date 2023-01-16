import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from Artikkel_Scraper import get_html

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

def read_urls(i):
    urls = []
    with open('urls.txt') as f:
        content = f.readlines()
        for count, line in enumerate(content):
            if count > i:
                return urls
            if not line:
                break
            urls.append(line.strip())
        f.close
    return urls

