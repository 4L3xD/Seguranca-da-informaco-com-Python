from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.infomoney.com.br/cotacoes/pao-de-acucar-pcar4/historico/').content
soup = BeautifulSoup(site, 'html.parser')
#print(soup.prettify())

table = soup.find("table", class_="default-table dataTable no-footer")
#print(soup.title.string)
print(soup.tr)
#print(soup.find('admin'))

number = 1888
variacao = requests.get('https://api.infomoney.com.br/ativos/ticker?type=json&_={}'.format(number)).content
soup2 = BeautifulSoup(variacao, 'html.parser')
print(variacao)