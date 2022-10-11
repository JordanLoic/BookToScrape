import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
reponse = requests.get(url)

page = reponse.content

soup = BeautifulSoup(page, "html.parser")

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











# """
# title = soup.find_all("li", class_="active")
# titre_livre = []
# for titre in title :
#     titre_livre.append(titre.text)
# print(titre_livre)
#
# description = soup.find_all("article" ,class_= "product_page")
# description_livre = []
# for descript in description :
#     description_livre.append(descript.text)
# print(description_livre[0])
# #titre = print(soup.h1.string)
#
# """
# """
# price = soup.find_all("p", class_="price_color")
# prix_livre = []
# for prix in price :
#     prix_livre.append(prix.text)
# print(prix_livre[0])
# """
# #print(price[0].text)
#
#
#
# information = soup.find_all("table", class_= "table-striped")
# info_textes = []
# for info in information :
#     info_textes.append(info.text)
# #print(info_textes)
#
# text = info_textes[0]
# print(text.replace("\n\n\n", ",").replace("\n\n", ",").replace("\n", ",").split(","))
#
#
# en_tete = ['Titre', 'Description', 'Information' , ]
# with open('data.csv', 'w') as csv_file :
#     writer = csv.writer(csv_file, delimiter =',')
#     writer.writerow(en_tete)
#     for Titre, Description, Information  in zip(titre_livre, description_livre, info_textes) :
#         writer.writerow([Titre, Description, Information])


""

"""
stock = soup.find_all("p", class_="instock availability")
stock_livre = []
for stockage in stock :
    stock_livre.append(stockage.text)
print(stock_livre[0])

#print(stock[0].text)
"""
