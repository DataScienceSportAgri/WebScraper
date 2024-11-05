from settings.settings import initialize_browser
from .html_fetcher import HTMLFetcher

from .page_navigator import PageNavigator

class BaseScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.driver = initialize_browser()
        self.html_fetcher = HTMLFetcher(self.driver)
        self.page_navigator = PageNavigator(self.base_url, self.html_fetcher)


    def close(self):
        if self.driver:
            self.driver.quit()