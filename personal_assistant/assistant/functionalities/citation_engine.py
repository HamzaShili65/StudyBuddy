import requests
from bs4 import BeautifulSoup
import datetime

class CitationEngine:
    def __init__(self):
        pass

    def cite_webpage(self, url, citation_style):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            title = soup.title.string if soup.title else self.ask_user("Title of Webpage")
            website_title = soup.find('meta', attrs={'property':'og:site_name'})
            website_title = website_title['content'] if website_title else self.ask_user("Website Title")
            pub_date = soup.find('meta', attrs={'property':'article:published_time'})
            pub_date = datetime.datetime.strptime(pub_date['content'], '%Y-%m-%dT%H:%M:%S+00:00').date() if pub_date else self.ask_user("Publication Date")
            
            if citation_style.lower() == 'mla':
                citation = f'"{title}". {website_title}, {pub_date}, {url}'
            elif citation_style.lower() == 'apa':
                citation = f'{title}. ({pub_date}). {website_title}. {url}'
            elif citation_style.lower() == 'chicago':
                citation = f'{title}. "{website_title}." {pub_date}. {url}'
            elif citation_style.lower() == 'turabian':
                citation = f'{title}. "{website_title}." {pub_date}. Accessed {access_date}. {url}'
            elif citation_style.lower() == 'ieee':
                citation = f'{title}. "{website_title}," {pub_date}. [Online]. Available: {url}. [Accessed: {access_date}]'
            else:
                citation = "Invalid citation style specified."

            return citation
        except Exception as e:
            print(f"An error occurred: {e}")
        return None

    def ask_user(self, prompt):
        return input(f"Please enter the {prompt}: ")

    #For MLA:
    def cite_book_mla(self, author, title, city, publisher, year):
        return f"{author}. {title}. {publisher}, {city}, {year}."

    def cite_paper_mla(self, author, title, journal, volume, issue, year, pages):
        return f"{author}. '{title}' {journal}, vol. {volume}, no. {issue}, {year}, pp. {pages}"

    def cite_image_mla(self, artist, title, year, medium, location):
        return f"{artist}. {title}. {year}, {medium}, {location}"

    def cite_video_mla(self, director, title, contributors, year, service):
        return f"{director}, dir. {title}. Perf. {contributors}, {service}, {year}"

    # For APA
    def cite_book_apa(self, author, year, title, publisher):
        return f"{author} ({year}). {title}. {publisher}."

    def cite_paper_apa(self, author, year, title, journal, volume, issue, pages):
        return f"{author} ({year}). {title}. {journal}, {volume}({issue}), {pages}."

    def cite_image_apa(self, artist, year, title, medium, url):
        return f"{artist} ({year}). {title} [{medium}]. {url}"

    def cite_video_apa(self, producer, year, title):
        return f"{producer} (Producer). ({year}). {title} [Video]."

    # For Chicago (note that the footnote and bibliography entries often differ)
    def cite_book_chicago(self, author, title, city, publisher, year):
        return f"{author}. {title}. {city}: {publisher}, {year}."

    def cite_paper_chicago(self, author, title, journal, volume, year, pages):
        return f"{author}. '{title}'. {journal} {volume}, (Year {year}): {pages}."

    def cite_image_chicago(self, artist, title, medium, year, url):
        return f"{artist}. {title}. {year}, {medium}. {url}"

    def cite_video_chicago(self, title, director, year):
        return f"{title}. Directed by {director}. {year}."

    # For Turabian (similar to Chicago, but with some differences)
    def cite_book_turabian(self, author, title, city, publisher, year):
        return f"{author}. {title}. {city}: {publisher}, {year}."

    def cite_paper_turabian(self, author, title, journal, volume, year, pages):
        return f"{author}. '{title}'. {journal} {volume}, no. (Year {year}): {pages}."

    def cite_image_turabian(self, artist, title, year, medium, url):
        return f"{artist}. {title}. {year}, {medium}. Accessed from {url}"

    def cite_video_turabian(self, title, director, year):
        return f"{title}. Directed by {director}. {year}."

    # For IEEE
    def cite_book_ieee(self, author, title, city, publisher, year):
        return f"[1] {author}, {title}. {city}: {publisher}, {year}."

    def cite_paper_ieee(self, author, title, journal, volume, issue, year, pages):
        return f"[1] {author}, '{title}', {journal}, vol. {volume}, no. {issue}, pp. {pages}, {year}."

    def cite_image_ieee(self, artist, title, year, medium, url):
        return f"[1] {artist}, {title}. {year}, {medium}. {url}"

    def cite_video_ieee(self, director, title, year):
        return f"[1] {title}, {director}, {year}."

