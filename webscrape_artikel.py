import requests
from bs4 import BeautifulSoup


class Artikkel:
    def __init__(self, URL):
        self.URL = URL
        page = requests.get(self.URL)
        self.soup = BeautifulSoup(page.content, "html.parser")
        self.text_elements = self.soup.find("div", class_="import-decoration u-mb32").p
        self.fasiliteter = self.soup.find("ul", class_="list list--bullets list--cols1to2 u-mb16").p

    #scrape fasilities
    




    #scrape the basic stats
    def scrape_stats(self):
        self.stats_dict = dict()
        stats = self.soup.find("dl", class_="definition-list definition-list--inline")
        stats_val = stats.find_all('dd')
        stats_key = stats.find_all('dt')
        
        for i in range(3):
            val = str(stats_val[i]).replace('<dd>', '').replace('</dd>', '').strip()
            key = str(stats_key[i]).replace('<dt>', '').replace('</dt>', '').strip()
            self.stats_dict[key] = val


        key = str(stats_key[-1]).replace('<dt>', '').replace('</dt>', '').strip()
        val = str(stats_val[-1]).split('"')
        val = val[1].split(':')
        self.stats_dict['Oppvarmingskarakter'] = val[-1].strip()
        val = val[1].split('.')
        self.stats_dict['Energikarakter'] = val[0].strip()

    def print_results(self):
        print(f'text elements : {self.text_elements}')
        print(f'fasiliteter {self.fasiliteter}')
        print(f'dict {self.stats_dict}')


A1 = Artikkel("https://www.finn.no/realestate/lettings/ad.html?finnkode=287010242")       
A1.scrape_stats()
A1.print_results()


       

#stats_svar = stats.find_all('dd')

#print(stats_svar)

#print(text_elements.p)

##dictinary = {"prompt": str(fasiliteter.text) +  " " + str(stats.text), "completion": text_elements.text}



        

