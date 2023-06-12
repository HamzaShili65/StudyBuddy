# functionalities/keyword_alert.py
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class KeywordAlert:
    def __init__(self, urls, keyword, output_file, check_interval=5*60):
        self.urls = urls
        self.keyword = keyword.lower()
        self.output_file = output_file
        self.check_interval = check_interval
        self.last_content = {url: None for url in urls}

    def check_page(self, url):
        response = requests.get(url)
        current_content = response.text
        if self.last_content[url] and self.keyword in current_content.lower() and current_content != self.last_content[url]:
            with open(self.output_file, 'a') as f:
                f.write(f"{datetime.now()}: ALERT: Keyword '{self.keyword}' found at {url}\n")
        self.last_content[url] = current_content

    def start_monitoring(self):
        while True:
            for url in self.urls:
                self.check_page(url)
            time.sleep(self.check_interval)
