import requests
from bs4 import BeautifulSoup

reponse = requests.get("http://books.toscrape.com/index.html")
page = reponse.content
soup = BeautifulSoup(page, "html.parser")

cat = soup.find("ul", class_="nav nav-list")
all_cat = cat.find_all("a")
#print(all_cat)
for links_cat in all_cat:
    #print(links_cat.get('href').replace('catalogue/', 'http://books.toscrape.com/catalogue/'))
    r_cat = requests.get(links_cat.get('href').replace('catalogue/', 'http://books.toscrape.com/catalogue/'))

    all_book = soup.find("ol", class_="row")
    all_url = all_book.find_all('a')

    for links in all_url:
        # print(links.get('href').replace('../../../', 'http://books.toscrape.com/catalogue/'))
        r = requests.get(links.get('href').replace('../../../', 'http://books.toscrape.com/catalogue/'))
        livres = r.content
        soup = BeautifulSoup(livres, "html.parser")

        # Extraction des information de chaque livre
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
