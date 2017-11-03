from bs4 import BeautifulSoup
from requests import get

url = 'https://br.pinterest.com/aallieennss/aircraft/'

agent = {'user-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'}
requisicao = get(url, headers=agent)
html = requisicao.text
soup = BeautifulSoup(html, 'html.parser')

imagens = soup.find_all('img')

for i in imagens:
    print(i)
    print('...\n...\n')
