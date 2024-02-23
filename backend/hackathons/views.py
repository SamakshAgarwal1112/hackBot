from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .scrapers.mlh_scraper import MLHScraper

# Create your views here.
class MLHEventsView(View):
    def get(self, request):
        scraper = MLHScraper()
        data = scraper.scrape()
        scraper.close()
        return JsonResponse(data,safe=False)