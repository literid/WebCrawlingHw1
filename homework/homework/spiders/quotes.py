import scrapy


class QuotesScraper(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    custom_settings = {"CONCURRENT_REQUESTS": 8, "CLOSESPIDER_ITEMCOUNT": 100}

    def start_requests(self):
        yield scrapy.Request(
            url="http://quotes.toscrape.com/", callback=self.parse_qoutes
        )

    def parse_qoutes(self, response):
        xpath = '//div[@class="col-md-8"]/div[@class="quote"]'
        for item in response.xpath(xpath):
            yield {
                "text": item.xpath(".//span[@class='text']/text()").get(),
                "author": item.xpath(".//small[@class='author']/text()").get(),
                "tags": item.xpath(
                    ".//div[@class='tags']/a[@class='tag']/text()"
                ).getall(),
            }

        if next_page := response.xpath(
            '//ul[@class="pager"]/li[contains(@class,"next")]/a/@href'
        ).get():
            yield scrapy.Request(
                url=response.urljoin(next_page), callback=self.parse_qoutes
            )
