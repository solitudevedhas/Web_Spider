import ssl
from queue import Queue
from Spider.Crawler.crawler import Crawler
from Spider.Crawler.crawler import *
from Spider.Crawler.crawler import *
from Spider.Crawler.crawler import *

# SystemT Inforamtion Extraction System


# Deal with SSL certification Error
ssl._create_default_https_context = ssl._create_unverified_context


PROJECT_NAME = 'Insurance_Info'
HOMEPAGE = 'https://www.iii.org/article/how-are-annuities-different-from-life-insurance'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/Task/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/Task/crawled.txt'

queue = Queue()

Crawler(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
print(Crawler.Database_dir)
