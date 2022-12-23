import logging
import requests
from bs4 import BeautifulSoup

# using this tutorial as a starting point:
# https://www.scrapingbee.com/blog/crawling-python/

class Crawler:

    def __init__(self, urls=[]):
        self.urls_on_page = []
        self.urls_to_visit = urls

    def add_urls_on_page(self, url):
        if url not in self.urls_on_page and url not in self.urls_to_visit:
            self.urls_on_page.append(url)



if __name__ == "__main__":
    Crawler(urls=['https://www.minecraft.net/en-us/download/server/bedrock']).run()
