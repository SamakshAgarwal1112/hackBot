from bs4 import BeautifulSoup as Soup
import requests as req
import socket

class USScraper:
    def __init__(self):
        socket.getaddrinfo('localhost',8000)
        self.url = "https://unstop.com/api/public/opportunity/search-result?opportunity=hackathons&page="
        
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
                    events_list['date'] = self.format_date(event['start_date'],event['end_date'])
                    events_list['url'] = event['seo_url'] if event['seo_url'] else "No Link"
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