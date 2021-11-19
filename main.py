# -*- coding: utf-8 -*-

# pip install requests
# pip install bs4
# Possible d'utiliser selenium mais il faudra connaitre le drivers
import requests
from bs4 import BeautifulSoup


# Effectuer une request http avec la méthode get
url = "https://fr.wikipedia.org/wiki/Liste_des_pays_du_monde"


if __name__ == "__main__":
    try:
        with open('./data/test.html') as fd:
            # print(f.read())
            soup = BeautifulSoup(fd, 'html.parser')

    except FileNotFoundError:
        print("Fichier introuvable")

    tab_body = soup.body.contents  # Recuperer tous les enfants de body

    print("Tous les enfants du body -->", tab_body)

    # Possible d'acceder au attribut d'une balise en traitant la balise comme un dictionnaire

    print("Id du first p -->", soup.p["id"])

    # Pour acceder directement au dictionnaire

    print("Dictionnaires contenant les attributs de p -->", soup.p.attrs)

    # Ajouter toutes les balises p dans un tableau

    print("Tous les paragraphes -->", soup.find_all("p"))

    #

    res = requests.get(url)
    if not res.ok:
        # Permet de parser et de chercher les elts à l'intérieur
        rep = BeautifulSoup(res.text, "html.parser")

        rep.prettify()
        print(rep.title)  # Affiche la balise title et son contenu

        print(rep.title.name)  # Affiche le nom de la balise

        print(rep.title.string)  # afficher  le contenu de la balise title

        print(rep.title.parent)  # Affiche le parent direct de title

        print(rep.p)  # Affiche le premier p dans toute la page

        print(rep.p["class"])  # Affiche la classe de p

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
