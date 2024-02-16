import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

page_request = requests.get(url)
html_content = page_request.text

soup = BeautifulSoup(html_content, "html.parser")

"""
Tag
bs4.element.Tag
"""
title = soup.title  # acessando a tag 'title'
print(type(title))  # o tipo de 'title' é tag
print(title.name)  # o nome de 'title' é title

footer = soup.footer  # acessando a tag 'footer'
print(footer["class"])  # acessando o atributo classe da tag footer

"""
NavigableString
bs4.element.NavigableString
"""
print(title.string)  # Acessando a string de uma tag
print(type(title.string))  # Verificando o tipo dessa string

"""
Navegando pela arvore
find: Primeira ocorrencia
find_all: Uma lista
"""

p_first = soup.find("p")
print(p_first)

p_all = soup.find_all("p")  # Lista as tags <p> existentes no documento
print(p_all)

print(soup.get_text())  # Todo o texto da página

"""
Buscar elemento pelo atributo class
"""
divs_attrs_class_quote = soup.find_all("div", attrs={"class": "alert"})
print(divs_attrs_class_quote)

divs_class_quote = soup.find_all(name="div", class_="alert")
print(divs_class_quote)
