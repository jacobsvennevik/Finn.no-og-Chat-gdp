from Artikkel_Scraper import Artikkel_Scraper
from url_getter import read_urls
import json
from time import sleep
from random import randint
from threading import Thread
import numpy as np
from safe_list import ThreadSafeList

def run_urls(url_li, data):
    for url in url_li:
        # mulig unødvendig med sleep siden jeg bruker multithreading blir brukt
        sleep(randint(2,30))
        scaper = Artikkel_Scraper(url)
        #få ut all info
        adr = scaper.find_el("span", "pl-4")
        fasiliteter = scaper.find_fas("div", "py-4 break-words")
        nokkelinfo = scaper.scrape_stats()
        skoleKollektiv_vei = scaper.find_kollektiv_skole()
        passerFor = scaper.find_passer_for("dp__cardContentListItem__3tbfT")
        kontaktPers = scaper.shadow_scrape("h3[aria-label='Kontaktperson']")
        #lage prompt
        prompt = f'Skriv en profesjonell salgsannonse på nettsiden Finn.no til en bolig med adresse: {adr}. Boligen har følgende fasiliteter {fasiliteter}. Boligen har følgende nøkkelinfo {nokkelinfo}. Det tar så lang tid å gå til diverse kollektivtransport: {skoleKollektiv_vei}. Naboloaget passer for {passerFor}og eiendomsmegleren er {kontaktPers} \n \n \n '
        #lager completion
        completion = scaper.find_text_with_breaks("div", "pt-16 sm:pt-40")

        info = {'prompt': prompt, 'completion': completion}
        data.append(info)



def do_split(lst, slices):
    return [sl.tolist()for sl in np.split(lst, slices)]

li = do_split(read_urls(1500), [150, 300, 450, 600, 750, 900])

safe_list = ThreadSafeList()
threads = [Thread(target=run_urls, args=(li[i], safe_list)) for i in range(len(li))]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

with open('plots.jsonl', 'w', encoding='utf-8') as outfile:
    for i in range(safe_list.length()):
        json.dump(safe_list.pop(), outfile, ensure_ascii=False)
        outfile.write('\n')




    
            
                