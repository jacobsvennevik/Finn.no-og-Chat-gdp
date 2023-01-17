import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from pyshadow.main import Shadow
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 




def get_html(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    return soup

class Artikkel_Scraper:
    def __init__(self, url):
        self.soup = get_html(url)
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.shadow = Shadow(self.driver)
        self.shadow.chrome_driver.get(url)

    #finner nøkkelinfo
    def find_fas(self, tag, name):
        tekst = []
        for t in self.soup.find_all(tag, class_= name):
            tekst.append(t.text)
        return tekst


    #finder element som tekst eller adressen
    def find_el(self, tag, name):
        return self.soup.find(tag, class_= name).text

    def find_text_with_breaks(self, tag, name):
        soup = BeautifulSoup(str(self.soup).replace('<br/>', '\n'), 'html.parser')
        return soup.find(tag, class_= name).text

    #SCRAPE fasiliteter balkong/tersasse osv
    def scrape_stats(self):
        stats_dict = dict()
        stats = self.soup.find("dl", class_="grid md:grid-cols-3 grid-cols-2 pb-8 gap-16 m-0")
        stats_val = stats.find_all('dd')
        stats_key = stats.find_all('dt')
    
        for i in range(len(stats) - 1):
            stats_dict[stats_key[i].text] = stats_val[i].text

        return stats_dict

    #nærmeste kollektiv og skole
    def find_kollektiv_skole(self):
        tilgjengelighet_dict = dict()
        ting = self.driver.find_elements(By.CLASS_NAME, 'dp__name__FmawV')
        tid = self.driver.find_elements(By.CLASS_NAME, 'dp__time__25gdB')
        for i in range(len(ting)-1):
            tilgjengelighet_dict[ting[i].text] = tid[i].text

        return tilgjengelighet_dict

    #Boks nede hvem passer nabolaget for?
    def find_passer_for(self, name):
        li = []
        for t in self.driver.find_elements(By.CLASS_NAME, name):
            li.append(t.text)
        return li

    #skraper ting som er i shadow
    def shadow_scrape(self, name):
        li = []
        elements = self.shadow.find_elements(name)
        for c in elements:
            c = c.text
            if c not in li:
                li.append(c)
        return li

 
""" def run():

    for url in read_urls(10):
        scaper = Artikkel_Scraper(url)
        print(scaper.find_el("div", "pt-16 sm:pt-40"))
        print(scaper.find_el("span", "pl-4"))
        print(scaper.find_fas("div", "py-4 break-words"))
        print(scaper.scrape_stats())
        print(scaper.find_kollektiv_skole())
        print(scaper.find_passer_for("dp__cardContentListItem__3tbfT"))
        print(scaper.shadow_scrape("h3[aria-label='Kontaktperson']"))

    


 
run() """



        

