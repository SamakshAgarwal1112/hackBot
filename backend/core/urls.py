"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from bookmarks.views import BookmarkViewSet
from hackathons.views import MLHEventsView, DFEventsView, DPEventsView, USEventsView, EventsView

router = routers.DefaultRouter()
router.register(r'bookmarks',BookmarkViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hackathons/',EventsView.as_view(),name='hackathons'),
    path('bookmarks/',include(router.urls)),
    path('mlh/',MLHEventsView.as_view(),name='mlh_events'),
    path('devfolio/',DFEventsView.as_view(),name='devfolio_events'),
    path('devpost/',DPEventsView.as_view(),name='devpost_events'),
    path('unstop/',USEventsView.as_view(),name='unstop_events'),
]
