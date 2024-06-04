import scrapy.spiders as sp, scrapy.linkextractors as le, test_scrape.items as items

class QuoteScrape(sp.Spider):
    name="quotescraper"
    start_urls=["https://quotes.toscrape.com/"]
    rules=(
        sp.Rule(le.LinkExtractor(restrict_css=".tags-box > .tag-item > a"), follow=True)
    )

    def parse(self, response):
        quote_item=items.TestScrapeQuote()

        for quote in response.css(".quote"):
            text=quote.css(".text::text").get()
            author=quote.css(".author::text").get()
            author_link=response.urljoin(quote.css("a::attr(href)").get())
            tags=quote.css(".tags .tag::text").extract()
            
            yield {
                'url': response.url,
                'text': text,
                'author': author,
                'author-link':author_link,
                'tags': tags
            }
        next_page = response.css(".next > a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        

