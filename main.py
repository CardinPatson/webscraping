# pip install requests
# pip install bs4
# Possible d'utiliser selenium mais il faudra connaitre le drivers
import requests
from bs4 import BeautifulSoup

# Effectuer une request http avec la méthode get
url = "https://fr.wikipedia.org/wiki/Liste_des_pays_du_monde"

res = requests.get(url)

if res.ok:
    # Permet de parser et de chercher les elts à l'intérieur
    rep = BeautifulSoup(res.text, "html.parser")

    rep.prettify()
    print(rep.title)

    # liste = rep.find_by_id("Pays_list.C3.A9s")

    # Preciser le parser que tu veux
    # print(rep.find("title"))

# print(res.headers)
# print(res.text)  #res.text si on veut afficher la pagesu
