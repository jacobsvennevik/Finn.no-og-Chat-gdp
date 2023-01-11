import requests
from bs4 import BeautifulSoup

url = 'https://www.finn.no/realestate/lettings/ad.html?finnkode=287010242'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Extract the title of the listing
title = soup.find('h1', class_='css-1gjih5z').get_text().strip()
print(title)

# Extract the price of the listing
price = soup.find('span', class_='css-1j7a64f').get_text().strip()
print(price)

# Extract the location of the listing
location = soup.find('span', class_='css-1c4zyw4').get_text().strip()
print(location)

# Extract the description of the listing
description = soup.find('section', class_='css-1v8xqci').get_text().strip()
print(description)
