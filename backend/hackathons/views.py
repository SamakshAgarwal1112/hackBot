from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
# from django.dispatch import Signal, receiver
from .scrapers.mlh_scraper import MLHScraper
from .scrapers.devfolio_scraper import DFScraper
from .scrapers.devpost_scraper import DPScraper
from .scrapers.unstop_scraper import USScraper
from rest_framework import viewsets
from .models import ScrapedHackathon
from .serializers import EventSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
import json

# events_fetched = Signal(providing_args=["events"])

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
    def get(self, request):
        scrapers = [MLHEventsView(), DFEventsView(), DPEventsView(), USEventsView()]
        all_events = []

        for event in scrapers:
            scraper_view = event.get(request).content.decode('utf-8')
            try:
                events_data = json.loads(scraper_view)
                all_events.extend(events_data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from {event}: {e}")

        for event_data in all_events:
            title = event_data.get('title')
            existing_instance = ScrapedHackathon.objects.filter(title=title).first()

            if existing_instance:
                print(f"Updating existing instance for {title}")
                # Update existing instance
                existing_instance.date = event_data.get('date')
                existing_instance.url = event_data.get('url')
                existing_instance.location = event_data.get('location')
                existing_instance.mode = event_data.get('mode')
                existing_instance.save()
            else:
                print(f"Creating new instance for {title}")
                # Create new instance
                ScrapedHackathon.objects.create(
                    title=event_data.get('title'),
                    date=event_data.get('date'),
                    url=event_data.get('url'),
                    location=event_data.get('location'),
                    mode=event_data.get('mode'),
                )

        return HttpResponse("All events fetched and processed successfully")

    
class EventViewSet(viewsets.ModelViewSet):
    queryset = ScrapedHackathon.objects.all().order_by('id')
    serializer_class = EventSerializer
    
    @action(detail=False, methods=['get'])
    def hackathons(self, request):
        # Call EventsView to fetch and process data
        events_view = EventsView()
        events_view.get(request)

        # Now fetch data from queryset and serialize it
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)