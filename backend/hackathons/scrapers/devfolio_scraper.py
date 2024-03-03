import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from ..proxies.proxies import get_data

class DFScraper:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.page_load_strategy = 'eager'
        self.options.binary_location = '/usr/bin/firefox'
        self.driver = webdriver.Firefox(options=self.options)
        self.id_url = "https://devfolio.co/hackathons/open"
        self.url = "https://devfolio.co/_next/data/"
        
    def get_unique_id(self):
        self.driver.get(self.id_url)
        try:
            script_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, '__NEXT_DATA__'))
            )
            
            json_data = json.loads(script_element.get_attribute('innerHTML'))
            build_id = json_data.get('buildId')
            return build_id

        except Exception as e:
            print(f'Error extracting unique ID: {e}')

        return None
    
    def format_date(self,start_date,end_date):
        start_month = start_date[5:7]
        end_month = end_date[5:7]
        start = start_date[8:10]
        end = end_date[8:10]
        months = {
            "01":"JAN","02":"FEB","03":"MAR","04":"APR","05":"MAY","06":"JUN","07":"JUL","08":"AUG","09":"SEP","10":"OCT","11":"NOV","12":"DEC"
        }
        return months[start_month]+" "+start+" - "+end if start_month==end_month else months[start_month]+" "+start+" - "+months[end_month]+" "+end
    
    def scrape(self):
        data_text = get_data(f'{self.url}{self.get_unique_id()}/hackathons.json')
        content = data_text._content.decode('utf-8')
        data = json.loads(content)
        all_events = []
        for event in data["pageProps"]["dehydratedState"]["queries"][0]["state"]["data"]["open_hackathons"]:
            events_list = dict()
            events_list['title'] = event['name']
            events_list['date'] = self.format_date(event['starts_at'],event['ends_at'])
            events_list['url'] = event['settings']['site'] if event['settings']['site'] else "No Link"
            events_list['location'] = "Not specified"
            events_list['mode'] = event['is_online'] if event['is_online'] else "Offline"
            all_events.append(events_list)
        self.close()
        return all_events
            
    def close(self):
        self.driver.close()

# Usage:
# scraper = DFScraper()
# data = scraper.scrape()
# print(data)