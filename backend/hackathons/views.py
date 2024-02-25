from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .scrapers.mlh_scraper import MLHScraper
from .scrapers.devfolio_scraper import DFScraper
from .scrapers.devpost_scraper import DPScraper
from .scrapers.unstop_scraper import USScraper
import json

# Create your views here.
class MLHEventsView(View):
    def get(self, request):
        scraper = MLHScraper()
        data = scraper.scrape()
        scraper.close()
        return JsonResponse(data,safe=False)
    
class DFEventsView(View):
    def get(self, request):
        scraper = DFScraper()
        data = scraper.scrape()
        return JsonResponse(data,safe=False)
    
class DPEventsView(View):
    def get(self, request):
        scraper = DPScraper()
        data = scraper.scrape()
        return JsonResponse(data,safe=False)

class USEventsView(View):
    def get(self, request):
        scraper = USScraper()
        data = scraper.scrape()
        return JsonResponse(data,safe=False)
    
class EventsView(View):
    def get(self,request):
        scrapers = [ MLHEventsView() , DFEventsView() , DPEventsView() , USEventsView() ]
        all_events = []
        for event in scrapers:
            scraper_view = event.get(request).content.decode('utf-8')
            all_events.extend(json.loads(scraper_view))
        return JsonResponse(all_events, safe=False)