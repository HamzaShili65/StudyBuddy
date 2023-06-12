# url_shortener.py
import pyshorteners

class URLShortener:
    def __init__(self):
        self.shortener = pyshorteners.Shortener()

    def shorten(self, url):
        return self.shortener.tinyurl.short(url)
