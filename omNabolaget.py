from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from webscrape_artikel import read_urls


urls = read_urls(10)
# instantiate options 
options = webdriver.ChromeOptions() 
 
# run browser in headless mode 
options.headless = True 
 
# instantiate driver 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 
 
# load website 

 
# get the entire website content 
driver.get(urls[0]) 

# select elements by class name 
def find_kollektiv_skole(driver):
    tilgjengelighet_dict = dict()
    ting = driver.find_elements(By.CLASS_NAME, 'dp__name__FmawV')
    tid = driver.find_elements(By.CLASS_NAME, 'dp__time__25gdB')
    for i in range(len(ting)-1):
        tilgjengelighet_dict[ting[i].text] = tid[i].text

    return tilgjengelighet_dict


def find_passer_for(driver, name):
    li = []
    for t in driver.find_elements(By.CLASS_NAME, name):
        li.append(t.text)
    return li



print(find_passer_for(driver, 'dp__cardContentListItem__3tbfT'))



