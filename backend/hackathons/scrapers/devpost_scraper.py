from ..proxies.proxies import get_data
import json

class DPScraper:
    def __init__(self):
        self.url = "https://devpost.com/api/hackathons?page="
    
    def scrape(self):
        try:
            for j in range(1,3):
                link = f'{self.url}{j}&per_page=10'
                data_text = get_data(link)
                content = data_text._content.decode('utf-8')
                data = json.loads(content)
                all_events = []
                for event in data['hackathons']:
                    events_list = dict()
                    events_list['title'] = event['title']
                    events_list['date'] = event['submission_period_dates']
                    events_list['url'] = event['url'] if event['url'] else "No Link"
                    events_list['location'] = "Not Specified"
                    events_list['mode'] = event['displayed_location']['location']
                    all_events.append(events_list)
                return all_events
        except Exception as e:
            print(e)

# Usage:
# scraper = DPScraper()
# data = scraper.scrape()
# print(data)