from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import requests


class Crawler:
    def __init__(self):
        self.urlbody = 'https://neolook.com'
        self.soup_parser = 'html.parser'

    def collectYears(self):
        archive = requests.get(urljoin(self.urlbody, 'archives'))
        soup = BeautifulSoup(archive.text, self.soup_parser)
        years = []
        for y in soup.select('div.sidebar > div.archives > ul > li > a'):
            parts = y.get('href').split('/')
            if len(parts) < 3:
                pass
            else:
                years.append(y.get('href'))
        return years

    def collectMonths(self, ayear):
        year = requests.get(urljoin(self.urlbody, ayear))
        soup = BeautifulSoup(year.text, self.soup_parser)
        months = []
        for m in soup.select('div.content > div > div > div > div.anchors > ul > li > a'):
            parts = m.get('href').split('/')
            months.append(m.get('href'))
        return months

    def collectDays(self, amonth):
        day = requests.get(urljoin(self.urlbody, amonth))
        soup = BeautifulSoup(day.text, self.soup_parser)
        days = []
        for d in soup.select('div.content > div > div > div > ul > li > a'):
            days.append(d.get('href'))
        return days

    def collectContent(self, aday):
        doc = requests.get(urljoin(self.urlbody, aday))
        soup = BeautifulSoup(doc.text, self.soup_parser)
        return soup.select('.layout > .content > .wrap > .archives > .description')[0]
