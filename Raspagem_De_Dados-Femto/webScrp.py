from bs4 import BeautifulSoup

import requests

url = "https://www.climatempo.com.br/"

html = requests.get(url).content

soup = BeautifulSoup(html, 'html5lib')

print(soup.prettify())
