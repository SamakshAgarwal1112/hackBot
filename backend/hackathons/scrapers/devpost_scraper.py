import requests as req
import socket

class DPScraper:
    def __init__(self):
        socket.getaddrinfo('localhost',8000)
        self.url = "https://devpost.com/api/hackathons?page="
    
    def scrape(self):
        try:
            for j in range(1,3):
                link = f'{self.url}{j}&per_page=10'
                data = req.get(link).json()
                # return data['hackathons']
                all_events = []
                for event in data['hackathons']:
                    events_list = dict()
                    events_list['title'] = event['title']
                    events_list['date'] = event['submission_period_dates']
                    events_list['url'] = event['url']
                    events_list['location'] = event['open_state']
                    events_list['mode'] = event['displayed_location']['location']
                    all_events.append(events_list)
                return all_events
                # for i in data['hackathons']:
                #     if(i['displayed_location']['location']!='Online'):
                #         print(i['title']," ",i['url']," ",i['displayed_location']['location']," ",i['themes']," ",i['prize_amount']," ",i['submission_period_dates']," ",i['organization_name'])
        except Exception as e:
            print(e)

# Usage:
# scraper = DPScraper()
# data = scraper.scrape()
# print(data)