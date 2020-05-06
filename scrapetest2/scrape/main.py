import sys

sys.path.append("/home/rc/Documents/scrapetest2")
sys.path.append("/home/rc/Documents/scrapetest2/scrape")

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer
import scrape.spiders.scpr as scpr
from scrapy.utils.project import get_project_settings
import scrape.FileRead as file
import scrape.urlGen as gen

print('============================= Initialising Spider ================================')

configure_logging()
settings = get_project_settings()
runner = CrawlerRunner(settings)

gen.walaurlgen()
gen.magicurlgen()


@defer.inlineCallbacks
def crawl():
    yield runner.crawl(scpr.scprSpider)
    yield runner.crawl(scpr.scprSpider1)
    reactor.stop()


crawl()
reactor.run()
file.ref_json()
