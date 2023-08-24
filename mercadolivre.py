import requests
from bs4 import BeautifulSoup

preparemnt = 'https://lista.mercadolivre.com.br/'
produtoName = str(input("Qual produto vc deseja? "))
response = requests.get(preparemnt+produtoName)

site = BeautifulSoup(response.text, "html.parser")
produtos = site.find_all('div', attrs={'class':'andes-card ui-search-result shops__cardStyles ui-search-result--core andes-card--flat andes-card--padding-16'})
for produto in produtos:
    titulo = produto.find('h2',attrs={'class':'ui-search-item__title shops__item-title'})
    link = produto.find('a',attrs={'class':'ui-search-item__group__element shops__items-group-details ui-search-link'})
    real  = produto.find('span',attrs={'class':'andes-money-amount__fraction'} )
    centavos = produto.find('span', attrs={'class':'andes-money-amount__cents'})
    # print(produto.prettify())
    print(titulo.text)
    print(link['href'])
    if (centavos):  
        print("Preço: R$:", real.text+','+centavos.text)
    else:
        print("Preço: R$:", real.text+',00')
    print()