from scraper.base_scraper import BaseScraper
def get_data_between(balises):

def finding_data_with_config(url, config):
    html = BaseScraper(url)
    def get_only_runners_html(html):
        balises = config.get_page_balise_runners()
        parsed_html = get_data_between(balises)
        return parsed_html
    parsed_html = get_only_runners_html(html)
    runners_data_page = parsed_html
    return runners_data_page