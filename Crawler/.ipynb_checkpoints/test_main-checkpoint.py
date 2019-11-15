import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'nintendo'
HOMEPAGE = 'https://www.nintendo.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/Data/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/Data/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()

Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)