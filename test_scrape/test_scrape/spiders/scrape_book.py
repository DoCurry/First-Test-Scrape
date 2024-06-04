import scrapy.spiders as sp, scrapy.linkextractors as le, test_scrape.items as items

class BookScrape(sp.CrawlSpider):
    name="bookscraper"
    start_urls=["https://books.toscrape.com/"]
    rules=(
        sp.Rule(le.LinkExtractor(restrict_css=".nav-list > li > ul > li > a"), follow=True),
        sp.Rule(le.LinkExtractor(restrict_css=".product_pod > .image_container > a"), callback="parse_book")
    )

    def parse_book(self, response):
        book_item=items.TestScrapeItem()

        book_item["image_url"] = response.urljoin(response.css(".item.active > img::attr(src)").get())
        book_item["title"] = response.css(".col-sm-6.product_main > h1::text").get()
        book_item["price"] = response.css(".price_color::text").get()
        book_item["upc"] = response.css(".table.table-striped > tr:nth-child(1) > td::text").get()
        book_item["url"] = response.url
        return book_item