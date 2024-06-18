import requests, bs4, pandas
tree={
    "Name": [],
    "Link":[]
}
def scrape(page):
    pages=requests.get(page)
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    
    main = soup.find("div", {"id":"content"})
    contents = main.find_all("article")
    pages = main.find("nav").find("div", {"class": "wp-pagenavi"})
    
    for content in contents:
        data = content.find("header").find("h2").find("a")
        print("Name: "+data.text.strip())
        print("Link: "+data.get("href"))
        tree["Name"].append(data.text.strip())
        tree["Link"].append(data.get("href"))
        print()
    
    next_page = pages.find("a", {"class":"nextpostslink"})
    if (next_page):
        return scrape(next_page.get("href"))
scrape("https://skidrowcodexgames.com/")
df = pandas.DataFrame(tree)
df.to_csv("test.csv", index=False