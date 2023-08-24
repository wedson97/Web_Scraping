import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

responses = requests.get('https://www.airbnb.com')



options = Options()
options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=options)

navegador.get('https://www.airbnb.com.br/')
time.sleep(0.5)
navegador.find_element(By.XPATH,'/html/body/div[5]/div/div/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/button').click()
time.sleep(0.5)
navegador.find_element(By.XPATH, '//*[@id="/homes-1-input"]').click()
time.sleep(0.5)

local = navegador.find_element(By.XPATH, '//*[@id="/homes-1-input"]')
local.send_keys("seattle")
local.submit()
time.sleep(0.5)
navegador.find_element(By.XPATH, '//*[@id="accordion-body-/homes-2"]/section/div/footer/button[1]').click()

mais = navegador.find_element(By.XPATH,'//*[@id="stepper-adults"]/button[2]')
mais.click()
time.sleep(0.5)
mais.click()

navegador.find_element(By.XPATH,'//*[@id="vertical-tabs"]/div[3]/footer/button[2]').click()
time.sleep(3)
page_contect = navegador.page_source

site = BeautifulSoup(page_contect,'html.parser')

resultados = []

hospedagens = site.findAll('div', attrs={'itemprop':'itemListElement'})
for hospedagem in hospedagens:
    descricao = hospedagem.find('meta', attrs={'itemprop': 'name'})
    url = hospedagem.find('meta',attrs={'itemprop': 'url'})
    titulo = hospedagem.find('div',attrs={'data-testid': 'listing-card-title'})
    preco = hospedagem.find('span',attrs={'class': 'a8jt5op dir dir-ltr'})

    resultados.append([titulo.text,descricao['content'],url['content'],preco.text])
planilha = pd.DataFrame(resultados, columns=['titulo','descricao','url','preco'])
print(planilha)
planilha.to_excel('Quartos disponiveis.xlsx',index=False)