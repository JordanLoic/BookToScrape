import requests
from bs4 import BeautifulSoup, SoupStrainer
import httplib2


url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
reponse = requests.get(url)

page = reponse.content
soup = BeautifulSoup(page, "html.parser")

# Extraction des URL
all_book = soup.find("ol", class_="row")
all_url = all_book.find_all('a')

for links in all_url:
    #print(links.get('href').replace('../../../', 'http://books.toscrape.com/catalogue/'))
    r = requests.get(links.get('href').replace('../../../', 'http://books.toscrape.com/catalogue/'))
    livres= r.content
    soup = BeautifulSoup(livres, "html.parser")


    #Extraction des information de chaque livre
    product_main = soup.find("div", class_="product_main")
    title = product_main.find("h1").text
    print(title)

    product_description_id = soup.find("div", attrs={"id": "product_description"})
    product_description = product_description_id.find_next('p').text
    print(product_description)
    product_gallery_id = soup.find("div", attrs={"id": "product_gallery"})
    product_gallery = product_gallery_id.find('img')

    print(product_gallery["src"].replace("../../", "http://books.toscrape.com/"))

    product_main_rating = product_main.find('p', attrs={"class": "star-rating"})
    print(product_main_rating["class"][1])
    gdp_table = soup.find("table", attrs={"class": "table-striped"})
    gdp_table_data = gdp_table.find_all_next("tr")

    table_data = {}
    for tr in gdp_table_data:
        th = tr.find('th').text
        td = tr.find('td').text
        table_data[th] = td
    print(table_data)

# links =[]
# for a in all_book.find_all('a', href=True):
#     if a.text:
#         links.append(a['href'])
# print(links)






# categorie = soup.find_all("li", class_="active")
# titre_categorie = []
# for titre in categorie:
#     titre_categorie.append(titre.text)
# print(titre_categorie)
#
# liste = soup.find_all("ol", class_="row")
# liste_categorie = []
# for listn in liste:
#     liste_categorie.append(listn.text.replace("\n\n\n\n\n\n\n\n\n\n\n\n\n", "").replace("\n\n\n    \n", "").replace("\n    \n\n", "").replace("\n\n", ",").replace("\n\n\n\n", ",").replace("\n", ","))
# print(liste_categorie)
#
# """
# name = soup.find_all("a")
# name_livre = []
# for nom in name:
#     name_livre.append(nom.text)
# print(name_livre)
# """
# """
# lien = soup.find_all("h3")
# lien_livre = []
# for link in lien:
#     lien_livre.append(link.text)
# print(lien_livre)
# """
#
# http = httplib2.Http()
# status, reponse = http.request(url)
# for link in BeautifulSoup(reponse, "html.parser", parse_only=SoupStrainer('a')):
#     if link.has_attr('href'):
#         print(link['href'])
#
# """
# info_lien = []
# for j in link['href', 20]:
#     info_lien.append(j.text)
# print(info_lien)
# """
#
# en_tete = ["Titre_Cat", "Liste_Liv"]
# with open('data_c.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file, delimiter=',')
#     writer.writerow(en_tete)
#     for Titre_Cat, Liste_Liv in zip(titre_categorie, liste_categorie,):
#         writer.writerow([Titre_Cat, Liste_Liv])
