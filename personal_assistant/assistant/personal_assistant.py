# personal_assistant.py
#from .functionalities import FileOrganizer, GoogleSearcher
from .functionalities.file_organizer import FileOrganizer
from .functionalities.google_searcher import GoogleSearcher, ScheduledSearcher, FilterSearcher
from .functionalities.keyword_alert import KeywordAlert
from .functionalities.citation_engine import CitationEngine
from .functionalities.url_shortener import URLShortener
import threading
import datetime


class PersonalAssistant:
    def __init__(self):
        self.organizer = FileOrganizer()
        self.searcher = GoogleSearcher()
        self.citation_engine = CitationEngine()
        self.shortener = URLShortener()

    def organize_files(self, directory, extensions=None):
        self.organizer.organize_folder(directory, extensions)

    def google_search(self, query):
        self.searcher.search(query)

    def schedule_search(self, time_of_day, query):
        now = datetime.datetime.now()
        hours, minutes = map(int, time_of_day.split(":"))
        search_time = datetime.datetime(now.year, now.month, now.day, hours, minutes)
        # If the search time is already past, schedule for next day
        if now > search_time:
            search_time += datetime.timedelta(days=1)
        # Calculate the difference in seconds
        interval = int((search_time - now).total_seconds())
        scheduled_searcher = ScheduledSearcher(interval, query)
        thread = threading.Thread(target=scheduled_searcher.schedule_search)
        thread.start()
    
    def filtered_search(self, query, site=None, filetype=None, intitle=None):
        searcher = FilterSearcher(query, site=site, filetype=filetype, intitle=intitle)
        searcher.search()
    
    def start_keyword_alert(self, urls, keyword, output_file, check_interval=5*60):
        keyword_alert = KeywordAlert(urls, keyword, output_file, check_interval)
        thread = threading.Thread(target=keyword_alert.start_monitoring)
        thread.start()
    
    def generate_citation(self, citation_type, *args):
        citation_method = getattr(self.citation_engine, citation_type)
        return citation_method(*args)
    
    def shorten_url(self, url):
        return self.shortener.shorten(url)

