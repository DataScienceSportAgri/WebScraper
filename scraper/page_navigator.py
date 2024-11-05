class PageNavigator:
    def __init__(self, base_url, html_fetcher):
        self.base_url = base_url
        self.html_fetcher = html_fetcher

    def scrape_all_pages(self, selected_elements, page_number_position, data_extractor):
        results = []
        page_number = 1
        while True:
            page_url = self.base_url.replace(page_number_position, str(page_number))
            html = self.html_fetcher.fetch_html(page_url)
            if not html:
                break
            finishers_data = data_extractor.extract_finishers_data(html, selected_elements)
            if not finishers_data:
                break
            results.extend(finishers_data)
            page_number += 1
        return results