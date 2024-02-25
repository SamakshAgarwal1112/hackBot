from bs4 import BeautifulSoup as Soup
import requests as req
import socket

class USScraper:
    def __init__(self):
        socket.getaddrinfo('localhost',8000)
        self.url = "https://unstop.com/api/public/opportunity/search-result?opportunity=hackathons&page="
    
    def scrape(self):
        for j in range(1,3):
            try:
                link = f'{self.url}{j}&per_page=10&oppstatus=recent'
                data = req.get(link).json()
                # print(data)
                # return data['data']['data']
                all_events = []
                for event in data['data']['data']:
                    events_list = dict()
                    events_list['title'] = event['title']
                    events_list['date'] = event['start_date']
                    events_list['url'] = event['seo_url']
                    events_list['location'] = event['organisation']['name']
                    events_list['mode'] = event['region']
                    all_events.append(events_list)
                return all_events
                # for i in data['data']['data']:
                #     if(i['region']=='offline') and (i['regnRequirements']['reg_status']=='STARTED'):
                #         # print(i['title']," ",i['organisation']['name'])
                #         # print(i)
                #         print(i['title']," ",i['type']," ",i['subtype']," ",i['organisation']['name']," ",i['seo_url']," ",i['status']," ",i['isPaid']," ",i['end_date']," ",i['start_date']," ",i['region']," ",i['regnRequirements']['start_regn_dt']," ",i['regnRequirements']['end_regn_dt']," ",i['regnRequirements']['reg_status']," ")
                #         li = list(i['prizes'])
                #         for i in li:
                #             print(i['rank']," ",i['cash']," ",i['currency']," ",i['certificate']," ")
            except Exception as e:
                print(e)

# Usage:
# scraper = USScraper()
# data = scraper.scrape()
# print(data)