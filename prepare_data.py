from Artikkel_Scraper  import Artikkel_Scraper 
from url_getter import read_urls
import json
from time import sleep
from random import randint
from threading import Thread
import numpy as np

def run_urls(url_li):
    with open('plots.jsonl', 'a') as outfile: 
        for url in url_li:
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

            #legger allt i json
            json.dump(info, outfile)
            outfile.write('\n')
    outfile.close()



def do_split(lst, slices):
    return [sl.tolist()for sl in np.split(lst, slices)]







if __name__ == '__main__':
    li = do_split(read_urls(1000), [150, 300, 450, 600, 750, 900])
    thread1 = Thread(target=run_urls, args=[li[0]])
    thread2 = Thread(target=run_urls, args=[li[1]])
    thread3 = Thread(target=run_urls, args=[li[2]])
    thread4 = Thread(target=run_urls, args=[li[3]])
    thread5 = Thread(target=run_urls, args=[li[4]])
    thread6 = Thread(target=run_urls, args=[li[5]])
    thread7 = Thread(target=run_urls, args=[li[6]])

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join() 
    thread7.join() 
            
                