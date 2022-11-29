import requests
from bs4 import BeautifulSoup

lapa = requests.get("https://vvsprogramm.github.io/2021_debug/")

# print(lapa)
# print(lapa.content)

soup = BeautifulSoup(lapa.content,'html.parser')

print(soup)
print(soup.prefix())

print(list(soup.children))

print(type (item)for item in list(soup.children))

html = list(soup.children)[2]

print(list(html.children))
