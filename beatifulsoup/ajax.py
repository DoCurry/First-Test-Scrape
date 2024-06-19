import bs4, requests

def scrape(page):
    pages = requests.get(page)
    soup = bs4.BeautifulSoup(pages.content, "html.parser")
    
    navs = soup.find("section", {"id":"oscars"}).find("div", {"class":"container"}).find_all("a", {"class":"year-link"})
    
    for nav in navs:
        year = nav.text.strip()
        data = requests.get("https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year="+year)

        print(data.json())

scrape("https://www.scrapethissite.com/pages/ajax-javascript/")