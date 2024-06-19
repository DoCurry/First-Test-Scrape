import bs4, requests, selenium
import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

http = "https://www.webscraper.io"

def load_all(page):
    driver = selenium.webdriver.Chrome()
    driver.maximize_window()
    driver.get(page)
    try:
        driver.find_element(By.ID, "closeCookieBanner").click()
        while True:
            try:
                load=driver.find_element(By.CLASS_NAME, "ecomerce-items-scroll-more")
                driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", load)
                load.click()
                driver.implicitly_wait(3)
            except NoSuchElementException:
                break
            except ElementNotInteractableException:
                break
        return driver
    except NoSuchElementException:
        return driver

def scrape(page):
    
    pages = load_all(page)
    
    soup = bs4.BeautifulSoup(pages.page_source, "html.parser")
        
    contents = soup.find("div", {"class": "container test-site"}).find("div", {"class":"row"}).find("div", {"class":"col-lg-9"}).find("div", {"class": "row"}).find_all("div", {"class":"product-wrapper card-body"})
    
    for content in contents:
        price=content.find("div", {"class":"caption"}).find("h4", {"class":"price"})
        name=price.find_next_sibling("h4").find("a", {"class":"title"})
        desc=price.find_next_sibling("p", {"class":"description"})
        review=content.find("div", {"class":"ratings"}).find("p", {"class":"review-count"})
        rating=review.find_next_sibling("p")
        
        print("Name: "+name.text.strip())
        print("Price: "+price.text.strip())
        print ("Description: "+desc.text.strip())
        print("Review Count: "+review.text.strip())
        print("Rating: "+str(rating.get("data-rating"))+" stars")
        print()
    
def scrapefrom(page):
    pages = requests.get(page)
    soup = bs4.BeautifulSoup(pages.content, "html.parser")
    c_nav = soup.find("ul", {"id":"side-menu"}).find("li", {"class":"nav-item active"})
    nav_links = c_nav.find_all("a", {"class":"nav-link"})
    for navl in nav_links:
        print("Now in "+navl.text.strip()+" Page")
        print("-"*20)
        scrape(http+navl.get("href"))
    if c_nav:
        next_nav = c_nav.find_next_sibling("li", {"class":"nav-item"}).find("a", {"class":"nav-link"})
        if next_nav:
            scrapefrom(http+next_nav.get("href"))
scrapefrom("https://www.webscraper.io/test-sites/e-commerce/more")