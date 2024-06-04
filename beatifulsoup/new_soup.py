import requests, bs4

def scrape(page):
    cp='https://books.toscrape.com/catalogue/'
    page = requests.get(cp+page)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    # catalogs=soup.find("div", {"class":"side_categories"}).find("ul", {'class':'nav nav-list'}).find("li").find("ul").find_all("li")

    # for catalog in catalogs:
    #     link = catalog.find("a")
    #     print ('Catalog Name:',link.text.strip())
    #     print(page.url+link.get("href"))
    #     print()

    books = soup.find("section").select("div:nth-child(2)")[0].find("ol").find_all("li")

    for book in books:
        name = book.find("article").find("h3").find("a")
        price = book.find("article").find("div", {"class":"product_price"}).find("p", {"class":"price_color"})
        stock = book.find("article").find("div", {"class":"product_price"}).find("p", {"class":"availability"})

        print('Book Name:', name.text.strip())
        print('Price:', price.text.strip())
        print('Stock', stock.text.strip())
        print(cp+name.get('href'))
        print()
    
    nextbtn=soup.find("ul", {"class":"pager"}).find("li", {"class":"next"}).find("a")
    if (nextbtn):
        return scrape(nextbtn.get('href'))
scrape('page-1.html')