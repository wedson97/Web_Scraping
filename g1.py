import requests
from bs4 import BeautifulSoup
import pandas as dp

lista_noticias = []

#pega o html da pagina
responde = requests.get('https://g1.globo.com')
site = responde.content

#trasforma bara um objeto da beautifulsoup
site = BeautifulSoup(site, 'html.parser')

#busca por partes especificas do html, (ELA PEGA APENAS A PRIMEIRA OCORRENCIA DA TAG, FINDALL PEGA TODAS)
post = site.find_all('div', attrs={'class':'feed-post-body'})

for noticia in post:
    resultado = noticia.find('a',attrs={'class':'feed-post-link gui-color-primary gui-color-hover'})
    
    subtitulo = noticia.find('div', attrs= {'class':'feed-post-body-resumo'})
    
    #printa o conteudo retornado
    
    if(subtitulo):
        lista_noticias.append([resultado.text, subtitulo.text, resultado['href']])
    else:
        lista_noticias.append([resultado.text, '',resultado['href']])


news = dp.DataFrame(lista_noticias, columns=['titulo', 'subtitulo', 'link'])
news.to_excel('Noticias.xlsx', index=False)
for i in range(len(lista_noticias)):
    print(lista_noticias[i][0])
    if(len(lista_noticias[i])==3):
        print(lista_noticias[i][1])
        print(lista_noticias[i][2])
    elif(len(lista_noticias[i])==2):
        print(lista_noticias[i][1])
    print("-----------------------------------------------------------------------")