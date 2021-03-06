from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from jobparser import settings
from jobparser.spiders.hhru import HhruSpider
from jobparser.spiders.superjob import SuperjobSpider

# I вариант
# 1) Доработать паука в имеющемся проекте, чтобы он формировал item по структуре:
# *Наименование вакансии
# *Зарплата от
# *Зарплата до
# *Ссылку на саму вакансию
# И складывал все записи в БД(любую)
#
# 2) Создать в имеющемся проекте второго паука по сбору вакансий с сайта superjob. Паук должен формировать
# item'ы по аналогичной структуре и складывать данные также в БД

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(HhruSpider)
    process.crawl(SuperjobSpider)

    process.start()

    pass