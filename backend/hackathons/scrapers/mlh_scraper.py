from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

class MLHScraper:
    def __init__(self):
        self.options = Options()
        self.options.page_load_strategy = 'eager'
        self.options.binary_location = '/usr/bin/firefox'
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.minimize_window()
        self.url = "https://mlh.io/seasons/2024/events"

    def scrape(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.row")))
        upcoming_events = self.driver.find_elements(By.CSS_SELECTOR, "div.row")[1]
        events = upcoming_events.find_elements(By.CSS_SELECTOR, "a.event-link")
        all_events = []
        for event in events:
            events_list = dict()
            events_list['title'] = event.find_element(By.CSS_SELECTOR, "h3.event-name").text
            events_list['date'] = event.find_element(By.CSS_SELECTOR, "p.event-date").text
            events_list['url'] = event.get_attribute("href")
            events_list['location'] = event.find_element(By.CSS_SELECTOR, "div.event-location").text
            events_list['mode'] = event.find_element(By.CSS_SELECTOR, "div.event-hybrid-notes").text
            all_events.append(events_list)
        return all_events

    def close(self):
        self.driver.close()

# Usage:
# scraper = MLHScraper()
# data = scraper.scrape()
# scraper.close()
# print(data)