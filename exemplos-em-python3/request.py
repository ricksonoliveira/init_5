from bs4 import BeautifulSoup
import requests

r = requests.get('https://pt.wikipedia.org/wiki/Brasil')
soup = BeautifulSoup(r.content, "lxml")

print(soup.title.text)























#
