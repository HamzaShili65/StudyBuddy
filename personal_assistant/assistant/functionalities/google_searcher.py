# google_searcher.py
import webbrowser
import time

class GoogleSearcher:
    def __init__(self, num_results=10):
        self.num_results = num_results

    def search(self, query):
        url = f"https://www.google.com/search?q={query}"
        try:
            webbrowser.open_new_tab(url)
        except Exception as e:
            print(f"An error occurred: {e}")


class ScheduledSearcher(GoogleSearcher):
    def __init__(self, interval, query):
        super().__init__()
        self.interval = interval
        self.query = query

    def schedule_search(self):
        sleep_time = self.interval
        time.sleep(sleep_time)
        super().search(self.query)
        # After the first search, set the interval to 24 hours (in seconds)
        #sleep_time = 24*60*60

class FilterSearcher(GoogleSearcher):
    def __init__(self, query, site=None, filetype=None, intitle=None):
        super().__init__()
        self.query = query
        self.site = site
        self.filetype = filetype
        self.intitle = intitle

    def search(self):
        url = f"https://www.google.com/search?q={self.query}"
        if self.site:
            url += f"+site:{self.site}"
        if self.filetype:
            url += f"+filetype:{self.filetype}"
        if self.intitle:
            url += f"+intitle:{self.intitle}"
        try:
            webbrowser.open_new_tab(url)
        except Exception as e:
            print(f"An error occurred: {e}")

