# import scrapy
# from urllib.parse import urlencode
# from scrapy.http import HtmlResponse
#
# from store_parser.items import StoreParserItem
#
# class AvitoSpider(scrapy.Spider):
#     name = 'avito'
#     allowed_domains = ['avito.ru']
#     start_urls = ['http://avito.ru/']
#
#     def __init__(self, name=None, **kwargs):
#         super().__init__(name, **kwargs)
#         self.start_urls = [f"http://avito.ru/{kwargs.get('region')}?{urlencode(kwargs.get('url_args'))}"]
#
#     def parse(self, response: HtmlResponse):
#         print()
#         items_links = response.xpath("//a[contains(@class, 'product-card__name')]")
#         for link in items_links:
#             yield response.follow(link, callback=self.parse_ads)
#
#     def parse_ads(self, response: HtmlResponse):
#         print()
#         name = response.xpath("//h1[contains(@class, 'product-essential__name')]/text()").get()
#         url = response.url
#         price = response.xpath("//div[contains(@class, 'add-to-cart__price')]//span[@class='price']//text()").getall()
#
#         # Доделать после того как появится решение 403 ошибки (Защита от DDoS на avito)!!!!!
#         # photos =
#         pass
