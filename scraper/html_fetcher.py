from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class HTMLFetcher:
    def __init__(self, driver):
        self.driver = driver

    def fetch_html(self, url):
        try:
            self.driver.get(url)

            # Wait for the body to be present
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            # Scroll to load all content
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            while True:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            return self.driver.page_source
        except Exception as e:
            print(f"Error fetching page {url}: {e}")
            return None