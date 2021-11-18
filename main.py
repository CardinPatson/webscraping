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
    print(rep.title.string)  # afficher  le contenu de la balise

    print(rep.find_all("a"))  # rechercher toutes les balises <a>

    print(rep.find(id="États_dont_la_souveraineté_est_contestée"))

    # Preciser le parser que tu veux
    # print(rep.find("title"))

    # extract url in <a> tag in a page
    for link in rep.find_all('a'):
        print(link.get("href"))

    text_page = rep.get_text()  # extraire tous le texte de la page

    # ==================================
    # NAVIGER A PARTIR DES NOM DES TAGS
    # ==================================

    # .content and .children
    print(rep.body)

    # Met tout ce qui se trouve dans le head dans un tableau
    print(rep.head.content)

    # iterer sur les balises enfants
    for child in rep.head.children:
        print(child)


# print(res.headers)
# print(res.text)  #res.text si on veut afficher la pagesu
