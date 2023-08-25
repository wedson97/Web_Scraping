import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.br/s?k='
produto = str(input("Qual produto deseja: "))
navegador = requests.get(url+produto)
navegador = BeautifulSoup(navegador.text, "html.parser")

#pega todas as divs que tem esse atributo (cards)
pesquisas = navegador.find_all('div', attrs={'data-component-type':'s-search-result'})

#Intera sobe cada div e pega os elementos desejados
for pesquisa in pesquisas:
    #Em todo span com essa classe, pega o titulo
    titulo = pesquisa.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
    #Em todo span com essa classe, pega o preco
    preco = pesquisa.find('span', attrs={'class':'a-offscreen'})
    #Em todo hiperlink com essa classe, pega o link
    url = pesquisa.find('a', attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    print(titulo.text)
    print(preco.text)
    print('https://www.amazon.com.br'+url['href'])
    print()
