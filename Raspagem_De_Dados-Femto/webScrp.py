import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://www.climatempo.com.br/"

cntent = requests.get(url).content

site = BeautifulSoup(cntent, 'html.parser')

found = site.find("h1")

# print(site.prettify())
print(found)
