import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.br/s?k='
produto = str(input("Qual produto deseja: "))
navegador = requests.get(url+produto)
navegador = BeautifulSoup(navegador.text, "html.parser")

pesquisas = navegador.find_all('div', attrs={'data-component-type':'s-search-result'})
for pesquisa in pesquisas:
    titulo = pesquisa.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
    preco = pesquisa.find('span', attrs={'class':'a-offscreen'})
    url = pesquisa.find('a', attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    print(titulo.text)
    print(preco.text)
    print('https://www.amazon.com.br'+url['href'])
    print()