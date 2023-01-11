import logging
import requests
import scrapy
from bs4 import BeautifulSoup

# Globals
URL = "https://www.minecraft.net/en-us/download/server/bedrock"

if __name__ == "__main__":
    page = requests.get(URL)
    print(page.status_code)
    print(page)
