from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from store_parser.spiders.castorama import CastoramaSpider
# from store_parser.spiders.avito import AvitoSpider

if __name__ == '__main__':
    configure_logging()
    settings = get_project_settings()
    runner = CrawlerRunner(settings)

    # Можно передавать параметры в url. Все что после "?" в url записывается в url_args.
    runner.crawl(
        CastoramaSpider,
        url_args={
            'q': 'смесители',
            'bm_tip_produkta': 'Смеситель для кухни'
        }
    )

    # runner.crawl(
    #     AvitoSpider,
    #     region='moskva',
    #     url_args={'q': 'кендо'}
    # )

    # d = runner.join()
    # d.addBoth(lambda x: reactor.stop())

    reactor.run()
