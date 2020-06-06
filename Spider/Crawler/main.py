# import ssl
# import threading
# from queue import Queue
# from web_spider.spider import Spider
# from web_spider.domain import *
# from web_spider.general import *


# Deal with SSL certification Error
ssl._create_default_https_context = ssl._create_unverified_context

PROJECT_NAME = 'Insurance_Info'
HOMEPAGE = 'https://www.iii.org/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/Data/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/Data/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()

Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


create_workers()
crawl()